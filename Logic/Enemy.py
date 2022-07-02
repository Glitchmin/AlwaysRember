from enum import Enum

import pygame as pygame

from Logic.Player import Player
from Logic.AbstractNPC import AbstractNPC

babol_texture = pygame.image.load(open("textures/enemy.png"))


class SearchType(Enum):
    SIGHT = 0
    HEARING = 1
    SMELL = 2


class EnemyTypes(Enum):
    BABOL = 0

    @property
    def texture(self) -> pygame.surface.Surface:
        match self:
            case EnemyTypes.BABOL:
                return babol_texture

    @property
    def searchType(self) -> SearchType:
        match self:
            case EnemyTypes.BABOL:
                return SearchType.HEARING

    @property
    def hp(self) -> int:
        match self:
            case EnemyTypes.BABOL:
                return 10

    @property
    def searchRadius(self) -> int:
        match self:
            case EnemyTypes.BABOL:
                return 5

    @property
    def name(self) -> str:
        match self:
            case EnemyTypes.BABOL:
                return "Babol"


class Enemy(AbstractNPC):
    def __init__(
        self, x: int, y: int, move_cooldown: float, type: EnemyTypes, player: Player
    ):
        super().__init__(type.hp, x, y, move_cooldown, type.texture)
        self.searchRadius = type.searchRadius
        self.searchType = type.searchType
        self.player = player
        self.name = type.name

    def make_move(self):
        if self.searchType == SearchType.HEARING:
            if (self.position[0] + self.player.position[0]) ** 2 + (
                self.position[1] + self.player.position[1]
            ) ** 2 <= self.searchRadius**2:
                pass
                # move yourself in the player direction
