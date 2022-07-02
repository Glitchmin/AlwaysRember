from enum import Enum

import pygame as pygame

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import AbstractItem
from helpers import load_resource, load_texture


class TileType(Enum):
    GROUND = 0
    STONE = 1
    BASE = 2

    def __init__(self, num: int):
        self.ground_texture = load_texture("ground.png")
        self.stone_texture = load_texture("stone.png")
        self.base_texture = load_resource("czaszka1.png")

    @property
    def texture(self) -> pygame.surface.Surface:
        match self:
            case TileType.GROUND:
                return self.ground_texture
            case TileType.STONE:
                return self.stone_texture
            case TileType.BASE:
                return self.base_texture
    @property
    def walkable(self) -> bool:
        match self:
            case TileType.GROUND:
                return True
            case TileType.STONE:
                return False
            case TileType.BASE:
                return True


class Tile:
    def __init__(self, tileType: TileType):
        self.__tileType: TileType = tileType
        self.__npc: AbstractNPC | None = None
        self.item: AbstractItem | None = None

    @property
    def tileType(self):
        return self.__tileType

    @property
    def npc(self):
        return self.__npc

    @npc.setter
    def npc(self, npc: AbstractNPC | None):
        self.__npc = npc

    @tileType.setter
    def tileType(self, value: TileType):
        self.__tileType = value
