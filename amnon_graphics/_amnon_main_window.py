from __future__ import annotations

from functools import partial
from pathlib import Path
from typing import Optional
from uuid import uuid4

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QLineEdit

from . import colors
from . import layouts
from .amnon_button import AmnonButton
from .amnon_label import AmnonLabel
from .amnon_text_box import AmnonTextBox

ElementId = str


class AmnonMainWindow(QMainWindow):
    WIDGET_ID_PROPERTY = 'id'
    """
    Wrapping PyQT5 main window object.
    manages the main window of the app
    """

    def __init__(self, name: str, height: int, width: int, background_color):
        super().__init__()
        self.setWindowTitle(name)
        self.setGeometry(0, 0, width, height)
        self.setStyleSheet(f"background-color: {background_color};")
        self._add_element_functions = []
        self._labels = []
        self._buttons = []
        self._text_boxes = []

    def _add_button(self, button: AmnonButton, uuid: Optional[str]) -> QPushButton:
        q_button = QPushButton(button.text, self)
        q_button.setGeometry(button.x_pos, button.y_pos, button.width, button.height)
        q_button.clicked.connect(partial(button.on_click, *button.on_click_params))
        q_button.setProperty(self.WIDGET_ID_PROPERTY, uuid or str(uuid4()))

        border_color = colors.GRAY if button.background_color != colors.GRAY else colors.WHITE
        q_button.setStyleSheet(
            "QPushButton"
            "{"
            f"background-color: {button.background_color};"
            "border-radius: 3px;"
            "}"
            "QPushButton:pressed"
            "{"
            f"border: 1px solid {border_color};"
            "}"
        )
        if button.image_path:
            q_button.setIcon(QIcon(str(button.image_path)))
            q_button.setIconSize(QSize(button.width, button.height - 20))
        self._buttons.append(q_button)
        return q_button

    def prepare_button(self, amnon_button: AmnonButton) -> ElementId:
        """Add the given button to the list of elements to be added later"""
        uuid = str(uuid4())
        self._add_element_functions.append(partial(self._add_button, amnon_button, uuid))
        return uuid

    def add_button(self, amnon_button: AmnonButton) -> ElementId:
        uuid = str(uuid4())
        new_button = self._add_button(amnon_button, uuid)
        new_button.show()
        return uuid

    def _add_label(self, label: AmnonLabel, uuid: Optional[str] = None) -> QLabel:
        q_label = QLabel(label.text, self)
        q_label.setGeometry(label.x_pos, label.y_pos, label.width, label.height)
        q_label.setStyleSheet(f'color: {label.text_color};')
        q_label.setStyleSheet(f"background-color: {label.background_color};"
                              f"border-radius: 3px")
        q_label.setAlignment(Qt.AlignCenter)
        q_label.setFont(QFont("Arial", label.font_size))
        if label.image_path:
            pixmap = QPixmap(str(label.image_path))
            q_label.setScaledContents(True)
            q_label.setPixmap(pixmap)
        q_label.setProperty(self.WIDGET_ID_PROPERTY, uuid or str(uuid4()))
        q_label.show()
        self._labels.append(q_label)
        return q_label

    def prepare_label(self, amnon_label: AmnonLabel) -> ElementId:
        """Add the given label to the list of elements to be added later"""
        uuid = str(uuid4())
        self._add_element_functions.append(partial(self._add_label, amnon_label, uuid))
        return uuid

    def add_label(self, amnon_label: AmnonLabel) -> ElementId:
        uuid = str(uuid4())
        new_label = self._add_label(amnon_label, uuid)
        new_label.show()
        return uuid

    def _add_text_box(self, amnon_text_box: AmnonTextBox, uuid: Optional[str] = None) -> QLineEdit:
        q_text_box = QLineEdit(self)
        q_text_box.move(amnon_text_box.x_pos, amnon_text_box.y_pos)
        q_text_box.resize(amnon_text_box.width, amnon_text_box.height)
        q_text_box.setStyleSheet(f'color: {amnon_text_box.text_color};')
        q_text_box.setStyleSheet(f"background-color: {amnon_text_box.background_color};"
                                 f"border-radius: 3px")

        q_text_box.textChanged.connect(partial(amnon_text_box.on_change, uuid, *amnon_text_box.on_change_params))
        q_text_box.setProperty(self.WIDGET_ID_PROPERTY, uuid or str(uuid4()))
        q_text_box.show()
        self._text_boxes.append(q_text_box)
        return q_text_box

    def prepare_text_box(self, amnon_text_box: AmnonTextBox) -> ElementId:
        """Add the given text box to the list of elements to be added later"""
        uuid = str(uuid4())
        self._add_element_functions.append(partial(self._add_text_box, amnon_text_box, uuid))
        return uuid

    def add_text_box(self, amnon_text_box: AmnonTextBox) -> ElementId:
        """Add the given text-box to the list of elements to be added later"""
        uuid = str(uuid4())
        new_text_box = self._add_text_box(amnon_text_box, uuid)
        new_text_box.show()
        return uuid

    def add_elements(self):
        """
        Calls all the functions that were added to self._add_element_functions every time that an element was
        requested to be added.
        The actual creation of the elements is delayed to run here so that the background is guaranteed to be
        created first.
        """
        for add_element_function in self._add_element_functions:
            add_element_function()

    def set_background_image(self, background_image_path: Path):
        """
        Directly add the background label to the window, without the indirection of adding it to
        self._add_element_functions.
        This ensures that the background is added first and actually appears in the background.
        """
        new_label = AmnonLabel(position=layouts.Position(self.geometry().x(), self.geometry().y()),
                               size=layouts.Size(self.width(), self.height()),
                               image_path=background_image_path)
        self._add_label(new_label)

    def get_widget_by_id(self, widget_id: ElementId) -> QWidget:
        """Get the widget (element) with the given element-id"""
        for widget in self._labels + self._buttons + self._text_boxes:
            if widget.property(self.WIDGET_ID_PROPERTY) == widget_id:
                return widget
