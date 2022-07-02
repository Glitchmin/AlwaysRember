from pygame.surface import Surface

from Logic.AbstractNPC import AbstractNPC


class Player(AbstractNPC):
    def __init__(self, hp: int, x: int, y: int, move_cooldown: float, texture: Surface):
        super().__init__(hp, x, y, move_cooldown, texture)
        self.leftHand = None
        self.rightHand = None
        self.backHand = None
