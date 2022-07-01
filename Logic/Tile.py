from enum import Enum

from Logic.AbstractNPC import AbstractNPC

walkable = [False, True]


class TileType(Enum):
    GRASS = 0
    BUILDING = 1


class Tile:
    def __init__(self, tileType: TileType):
        self.__tileType = tileType
        self.__npcsTab: [AbstractNPC] = []
        self.item = None
