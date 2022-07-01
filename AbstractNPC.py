from DirectionsEnum import Direction


class AbstractNPC:
    def __init__(self, hp, x, y):
        self.__hp = hp
        self.__x = x
        self.__y = y

    def move(self, dir: Direction):
        self.__x -= dir[0]
        self.__y -= dir[1]


