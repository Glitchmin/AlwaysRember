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
    BABOL_SMELL = 1

    @property
    def texture(self) -> pygame.surface.Surface:
        match self:
            case EnemyTypes.BABOL:
                return babol_texture
            case EnemyTypes.BABOL_SMELL:
                return babol_texture

    @property
    def searchType(self) -> SearchType:
        match self:
            case EnemyTypes.BABOL:
                return SearchType.HEARING
            case EnemyTypes.BABOL_SMELL:
                return SearchType.SMELL

    @property
    def hp(self) -> int:
        match self:
            case EnemyTypes.BABOL:
                return 10
            case EnemyTypes.BABOL_SMELL:
                return 10

    @property
    def searchRadius(self) -> int:
        match self:
            case EnemyTypes.BABOL:
                return 5
            case EnemyTypes.BABOL_SMELL:
                return 8

    @property
    def name(self) -> str:
        match self:
            case EnemyTypes.BABOL:
                return "Babol"
            case EnemyTypes.BABOL_SMELL:
                return "Smelly Babol"

    @property
    def damage(self) -> int:
        match self:
            case EnemyTypes.BABOL:
                return 8
            case EnemyTypes.BABOL_SMELL:
                return 10


class Enemy(AbstractNPC):
    def __init__(
        self,
        x: int,
        y: int,
        move_cooldown: float,
        damage: int,
        type: EnemyTypes,
        player: Player,
    ):
        super().__init__(type.hp, x, y, move_cooldown, type.texture)
        self.searchRadius = type.searchRadius
        self.searchType = type.searchType
        self.player = player
        self.name = type.name
        self.damage = damage

    def detects(self, tileSet):
        if self.searchType == SearchType.HEARING:
            return (self.position[0] - self.player.position[0]) ** 2 + (
                self.position[1] - self.player.position[1]
            ) ** 2 <= self.searchRadius**2
        elif self.searchType == SearchType.SMELL:
            direction = tileSet.get_direction_to_player(self.position).value
            new_position = (
                self.position[0] + direction[0],
                self.position[1] + direction[1],
            )
            return (
                tileSet.dist_to_player[new_position[0]][new_position[1]]
                < self.searchRadius
            )

    def attack(self):
        if self.can_move():
            self.player.getDamaged(10)

            # TODO: singnal being damaged (sound/animation)
            # print(f'attacking player, hp{self.player.hp}')
