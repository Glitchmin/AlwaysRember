from pygame.surface import Surface
from Logic.Direction import Direction

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import AbstractItem


class Player(AbstractNPC):
    def __init__(self, hp: int, x: int, y: int, move_cooldown: float, texture: Surface):
        super().__init__(hp, x, y, move_cooldown, texture)
        self.leftHand: AbstractItem | None = None
        self.rightHand: AbstractItem | None = None
        self.backHand: AbstractItem | None = None
        self.wanted_direction: Direction | None = None
        self.second_wanted_direction: Direction | None = None

    def set_wanted_direction(self, direction: Direction):
        self.second_wanted_direction = self.wanted_direction
        self.wanted_direction = direction

    def remove_direction(self, direction: Direction):
        if self.second_wanted_direction == direction:
            self.second_wanted_direction = None
        elif self.wanted_direction == direction:
            self.wanted_direction = self.second_wanted_direction
            self.second_wanted_direction = None
