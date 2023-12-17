from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .layouts import Position, Size
from . import colors

@dataclass
class AmnonLabel:
    """A class containing all the information needed to create a label"""
    position: Position
    size: Size
    text: Optional[str] = None
    text_color: Optional[str] = colors.WHITE
    background_color: str = colors.BLUE
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
