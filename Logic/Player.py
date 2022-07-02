from Logic.Direction import Direction

from Logic.AbstractNPC import AbstractNPC
import Logic.Item as Items

import pygame as pygame


class Player(AbstractNPC):
    def __init__(
        self,
        hp: int,
        x: int,
        y: int,
        move_cooldown: float,
    ):
        super().__init__(
            hp,
            x,
            y,
            move_cooldown,
            pygame.image.load(open("textures/player.png")),
        )
        self.leftHand: Items.LightSource | None = Items.torch
        self.rightHand: Items.Weapon | None = Items.axe
        self.backHand: Items.AbstractItem | None = None
        self.screenX: int = 0
        self.screenY: int = 0
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
        self.screenX: int = 0
        self.screenY: int = 0
