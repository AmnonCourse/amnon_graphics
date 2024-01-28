from dataclasses import dataclass, field
from typing import Callable, List, Any, Union

from . import colors
from .colors import RGB
from .layouts import Position, Size


@dataclass
class AmnonTextBox:
    """
    A text box lets the user enter text, and triggers the callback method each time the text is changed

    If you want to pass parameters to the `on_change` callback method, define in `on_change_params`.

    The first argument of 'on_change' is always the id of the textbox that was change, in order to get the new text.

    Example:
    def textbox_on_changed(textbox_id, app):
        new_text = app.get_textbox_text(textbox_id)
        print(new_text)

    textbox = AmnonTextBox(
        position=layouts.Position(100, 100),
        size=layouts.Size(100, 20),
        on_change=textbox_on_changed,
        on_change_params=[app]
    )
    """
    position: Position
    size: Size
    on_change: Callable
    on_change_params: List[Any] = field(default_factory=list)
    text_color: Union[str, RGB] = colors.WHITE
    background_color: Union[str, RGB] = colors.BLUE

    @property
    def x_pos(self):
        return self.position.x_pos

    @x_pos.setter
    def x_pos(self, value):
        self.position.x_pos = value

    @property
    def y_pos(self):
        return self.position.y_pos

    @y_pos.setter
    def y_pos(self, value):
        self.position.y_pos = value

    @property
    def height(self):
        return self.size.height

    @property
    def width(self):
        return self.size.width
