from pygame.surface import Surface

from Logic.Direction import Direction


class AbstractNPC:
    def __init__(self, hp: int, x: int, y: int, texture: Surface):
        self.__hp = hp
        self.__x = x
        self.__y = y
        self.__texture = texture

    def move(self, dir: Direction):
        self.__x += dir.value[0]
        self.__y += dir.value[1]

    @property    
    def position(self) -> tuple[int, int]:
        return self.__x, self.__y
    @property        
    def texture(self) -> Surface:
        return self.__texture
