from enum import Enum

import pygame

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import Item

ground_texture = pygame.image.load(open("textures/ground.png"))
stone_texture = pygame.image.load(open("textures/stone.png"))

class TileType(Enum):
    GROUND = 0
    STONE = 1

    @property
    def texture(self) -> pygame.Surface:
        if self == TileType.GROUND:
            return ground_texture
        elif self == TileType.STONE:
            return stone_texture

    @property
    def walkable(self) -> bool:
        if self == TileType.GROUND:
            return True
        elif self == TileType.STONE:
            return False
    


class Tile:
    def __init__(self, tileType: TileType):
        self.__tileType = tileType
        self.__npc: AbstractNPC | None = None
        self.item: Item | None = None

    @property
    def tileType(self): 
        return self.__tileType

    @property
    def npc(self): 
        return self.__npc
    


