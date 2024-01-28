from dataclasses import dataclass

BLACK = 'black'
WHITE = 'white'
RED = 'red'
BLUE = 'blue'
GREEN = 'green'
YELLOW = 'yellow'
MAGENTA = 'magenta'
CYAN = 'cyan'
GRAY = 'gray'


@dataclass
class RGB:
    r: int
    g: int
    b: int

    def __str__(self):
        return f'rgb({self.r},{self.g},{self.b})'

    def __post_init__(self):
        if self.r < 0 or self.r > 255 or self.g < 0 or self.g > 255 or self.b < 0 or self.b > 255:
            raise ValueError(f'invalid color codes: {self.r},{self.g},{self.b}')
