from enum import Enum

import pygame as pygame

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import AbstractItem

ground_texture = pygame.image.load(open("textures/ground.png"))
stone_texture = pygame.image.load(open("textures/stone.png"))


class TileType(Enum):
    GROUND = 0
    STONE = 1

    @property
    def texture(self) -> pygame.surface.Surface:
        match self:
            case TileType.GROUND:
                return ground_texture
            case TileType.STONE:
                return stone_texture

    @property
    def walkable(self) -> bool:
        match self:
            case TileType.GROUND:
                return True
            case TileType.STONE:
                return False


class Tile:
    def __init__(self, tileType: TileType):
        self.__tileType = tileType
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
    def tileType(self, value):
        self._tileType = value
