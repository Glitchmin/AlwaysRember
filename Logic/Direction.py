from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)
    RIGHT = (1, 0)

    @property
    def x(self) -> int:
        return self.value[0]
    
    @property
    def y(self) -> int:
        return self.value[0]
