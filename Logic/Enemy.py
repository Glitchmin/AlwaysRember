from enum import Enum

from pygame.surface import Surface

from Logic import Player
from Logic.AbstractNPC import AbstractNPC


class SearchType(Enum):
    SIGHT = 0
    HEARING = 1
    SMELL = 2


class Enemy(AbstractNPC):
    def __init__(self, hp: int, x: int, y: int, texture: Surface, searchRadius: int, searchType: SearchType,
                 player: Player):
        super().__init__(hp, x, y, texture)
        self.searchRadius = searchRadius
        self.searchType = searchType
        self.player = player

    def makeMove(self):
        if self.searchType == SearchType.HEARING:
            if (self.getPosition()[0] + self.player.getPosition()[0]) ** 2 + \
                    (self.getPosition()[1] + self.player.getPosition()[1]) ** 2 <= self.searchRadius ** 2:
                pass
                # move yourself in the player direction
