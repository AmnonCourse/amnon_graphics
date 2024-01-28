from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from . import colors
from .colors import RGB
from .layouts import Position, Size


@dataclass
class AmnonLabel:
    """
    A label is used to display text or an image on the app.
    To display text use the `text` attribute
    To display an image use the `image_path` attribute
    """
    position: Position
    size: Size
    text: Optional[str] = None
    text_color: Union[str, RGB] = colors.WHITE
    background_color: Union[str, RGB] = colors.BLUE
    image_path: Optional[Path] = None
    font_size: int = 12

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
