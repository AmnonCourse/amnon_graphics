from dataclasses import dataclass


@dataclass
class Position:
    x_pos: int
    y_pos: int


@dataclass
class Size:
    width: int
    height: int
