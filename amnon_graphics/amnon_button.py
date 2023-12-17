from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Any, List

from .layouts import Position, Size
from . import colors

@dataclass
class AmnonButton:
    """A class containing all the information needed to create a button"""
    position: Position
    size: Size
    on_click: callable
    on_click_params: List[Any] = field(default_factory=list)
    text: Optional[str] = None
    background_color: str = colors.GRAY
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