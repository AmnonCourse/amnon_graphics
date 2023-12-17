from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .layouts import Position, Size


@dataclass
class AmnonButton:
    """A class containing all the information needed to create a button"""
    position: Position
    size: Size
    on_click: callable
    text: Optional[str] = None
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

    @property
    def width(self):
        return self.size.width
