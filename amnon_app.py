from inspect import signature
import sys
from pathlib import Path
from typing import Optional, Union

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

from ._amnon_main_window import AmnonMainWindow, ElementId
from .amnon_button import AmnonButton
from .amnon_label import AmnonLabel
from .amnon_text_box import AmnonTextBox
from . import colors
from .colors import RGB


class AmnonApp(QApplication):
    """
    Wrapping pyQT5 API
    """
    DEFAULT_HEIGHT = 1000
    DEFAULT_WIDTH = 800
    DEFAULT_NAME = 'App'
    
    def __init__(self, name: str = DEFAULT_NAME, height: Optional[int] = DEFAULT_HEIGHT, width: Optional[int] = DEFAULT_WIDTH,
                 background_color: Union[str, RGB] = colors.BLACK):
        """
        Initiating the app
        :param name: the app's name, will be the title of the main window
        """
        super().__init__([])
        self._is_running = False
        self._main_window = AmnonMainWindow(name, height=height, width=width, background_color=background_color)

    @property
    def window_width(self) -> int:
        return self._main_window.width()

    @property
    def window_height(self) -> int:
        return self._main_window.height()

    def add_button(self, button: AmnonButton) -> ElementId:
        """Adds a button to the app, that triggers a function when clicked."""
        expected_params_len = len(signature(button.on_click).parameters)
        num_of_supplied_params = len(button.on_click_params)
        if expected_params_len != num_of_supplied_params:
            raise ValueError(f'expected {expected_params_len} `on_click_params` but got {num_of_supplied_params}')

        if self._is_running:
            return self._main_window.add_button(button)
        return self._main_window.prepare_button(button)

    def add_label(self, label: AmnonLabel) -> ElementId:
        """
        Adds a label to the app.
        Labels can display text or an image and trigger no event when clicked.
        """
        if self._is_running:
            return self._main_window.add_label(label)
        return self._main_window.prepare_label(label)

    def add_textbox(self, text_box: AmnonTextBox) -> ElementId:
        """Adds a textbox to the app, that triggers a function whenever its content changes"""
        expected_params_len = len(signature(text_box.on_change).parameters) - 1 # remove one because `uuid` gets added automatically
        num_of_supplied_params = len(text_box.on_change_params)
        if expected_params_len != num_of_supplied_params:
            raise ValueError(f'expected {expected_params_len} `on_change_params` but got {num_of_supplied_params}\n'
                             f'Make sure that the first parameter of the `on_change` method is `uuid`, '
                             f'and isn\'t included in `on_change_params`')

        if self._is_running:
            return self._main_window.add_textbox(text_box)
        return self._main_window.prepare_text_box(text_box)

    def set_background_image(self, background_image_path: Path):
        """
        Sets the background image of the apps.
        This method adds a label in the size of the window, and ensures that it is created first
        so that it appears in the background.
        """
        self._main_window.set_background_image(background_image_path)

    def _get_element_by_id(self, widget_id: ElementId) -> QWidget:
        """Get an element according to the given element-id."""
        return self._main_window.get_widget_by_id(widget_id)

    def change_label_text(self, label_id: ElementId, new_text: str) -> None:
        """Change the text of the label with the given element-id"""
        label = self._get_element_by_id(label_id)
        label.setText(new_text)

    def get_textbox_text(self, textbox_id: ElementId) -> str:
        textbox: QLineEdit = self._get_element_by_id(textbox_id)
        return textbox.text()

    def remove_element(self, element_id: ElementId):
        """Remove an element from the window according to the given element-id."""
        element = self._get_element_by_id(element_id)
        element.setParent(None)

    def run(self):
        """
        Runs the app.
        This method should be called after adding all relevant elements to the window.
        """
        self._is_running = True
        self._main_window.add_elements()
        self._main_window.show()
        sys.exit(self.exec_())
