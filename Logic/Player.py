from pygame.surface import Surface

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import AbstractItem


class Player(AbstractNPC):
    def __init__(self, hp: int, x: int, y: int, move_cooldown: float, texture: Surface):
        super().__init__(hp, x, y, move_cooldown, texture)
        self.leftHand: AbstractItem | None = None
        self.rightHand: AbstractItem | None = None
        self.backHand: AbstractItem | None = None
