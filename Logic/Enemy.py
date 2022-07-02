from enum import Enum

import pygame
from pygame.surface import Surface

from Logic import Player
from Logic.AbstractNPC import AbstractNPC

babol_texture = pygame.image.load(open("textures/enemy.png"))


class SearchType(Enum):
    SIGHT = 0
    HEARING = 1
    SMELL = 2


class EnemyTypes(Enum):
    BABOL = 0

    @property
    def texture(self) -> pygame.Surface:
        if self == EnemyTypes.BABOL:
            return babol_texture

    @property
    def searchType(self) -> SearchType:
        if self == EnemyTypes.BABOL:
            return SearchType.HEARING

    @property
    def hp(self) -> int:
        if self == EnemyTypes.BABOL:
            return 10

    @property
    def searchRadius(self) -> int:
        if self == EnemyTypes.BABOL:
            return 5

    @property
    def name(self) -> str:
        if self == EnemyTypes.BABOL:
            return "Babol"


class Enemy(AbstractNPC):
    def __init__(self, x: int, y: int, move_cooldown: float, type: EnemyTypes, player: Player):
        super().__init__(type.hp, x, y, move_cooldown, type.texture)
        self.searchRadius = type.searchRadius
        self.searchType = type.searchType
        self.player = player
        self.name = type.name

    def makeMove(self):
        if self.searchType == SearchType.HEARING:
            if (self.position[0] + self.player.getPosition()[0]) ** 2 + (
                self.position[1] + self.player.getPosition()[1]
            ) ** 2 <= self.searchRadius**2:
                pass
                # move yourself in the player direction
