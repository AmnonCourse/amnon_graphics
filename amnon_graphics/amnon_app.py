import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QWidget

from ._amnon_main_window import AmnonMainWindow, ElementId
from .amnon_button import AmnonButton
from .amnon_label import AmnonLabel
from .amnon_text_box import AmnonTextBox


class AmnonApp(QApplication):
    """
    Wrapping pyQT5 API
    """

    def __init__(self, name: str):
        """
        Initiating the app
        :param name: the app's name, will be the title of the main window
        """
        super().__init__([])
        self._main_window = AmnonMainWindow(name)

    @property
    def window_width(self) -> int:
        return self._main_window.width()

    @property
    def window_height(self) -> int:
        return self._main_window.height()

    def add_button(self, button: AmnonButton) -> ElementId:
        """Adds a button to the app, that triggers a function when clicked."""
        return self._main_window.add_button(button)

    def add_label(self, label: AmnonLabel) -> ElementId:
        """
        Adds a label to the app.
        Labels can display text or an image and trigger no event when clicked.
        """
        return self._main_window.add_label(label)

    def add_textbox(self, text_box: AmnonTextBox) -> ElementId:
        """Adds a textbox to the app, that triggers a function whenever its content changes"""
        return self._main_window.add_text_box(text_box)

    def set_background_image(self, background_image_path: Path):
        """
        Sets the background image of the apps.
        This method adds a label in the size of the window, and ensures that it is created first
        so that it appears in the background.
        """
        self._main_window.set_background_image(background_image_path)

    def get_element_by_id(self, widget_id: ElementId) -> QWidget:
        """Get an element according to the given element-id."""
        return self._main_window.get_widget_by_id(widget_id)

    def change_label_text(self, label_id: ElementId, new_text: str):
        """Change the text of the label with the given element-id"""
        label = self.get_element_by_id(label_id)
        label.setText(new_text)

    def remove_element(self, element_id: ElementId):
        """Remove an element from the window according to the given element-id."""
        element = self.get_element_by_id(element_id)
        element.setParent(None)

    def run(self):
        """
        Runs the app.
        This method should be called after adding all relevant elements to the window.
        """
        self._main_window.add_elements()
        self._main_window.show()
        sys.exit(self.exec_())
