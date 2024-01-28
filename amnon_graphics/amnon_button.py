from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Any, List, Union

from . import colors
from .colors import RGB
from .layouts import Position, Size


@dataclass
class AmnonButton:
    """
    Define buttons to let the user interact with your app.

    The action that is executed when the button is pressed is the `on_click` methods.
    If you want to supply parameters to this function, use the `on_click_params` attribute.

    Example:
    def button_on_click(text):
        print(text)

    button = AmnonButton(
        position=layouts.Position(20, 45),
        size=layouts.Size(100, 50),
        on_click=on_click,
        on_click_params=['my message!!'],
        text='Print my message',
        background_color=colors.WHITE
    )
    """
    position: Position
    size: Size
    on_click: callable
    on_click_params: List[Any] = field(default_factory=list)
    text: Optional[str] = None
    background_color: Union[str, RGB] = colors.GRAY
    image_path: Optional[Path] = None

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

    @height.setter
    def height(self, value):
        if value > 0:
            self.size.height = value
        else:
            raise ValueError(f"invalid button height: {value}")

    @property
    def width(self):
        return self.size.width

    @width.setter
    def width(self, value):
        if value > 0:
            self.size.width = value
        else:
            raise ValueError(f"invalid button width: {value}")
