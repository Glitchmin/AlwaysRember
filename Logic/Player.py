from pygame.surface import Surface

from Logic.AbstractNPC import AbstractNPC
from Logic.Item import AbstractItem, LightSource, Weapon


class Player(AbstractNPC):
    def __init__(self, hp: int, x: int, y: int, move_cooldown: float, texture: Surface):
        super().__init__(hp, x, y, move_cooldown, texture)
        self.leftHand: LightSource | None = LightSource("torch", 4.0, 90)
        self.rightHand: Weapon | None = None
        self.backHand: AbstractItem | None = None
        self.screenX: int = 0
        self.screenY: int = 0
