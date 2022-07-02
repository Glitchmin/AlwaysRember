from Logic.Direction import Direction

from Logic.AbstractNPC import AbstractNPC
import Logic.Item as Items

import pygame as pygame

from helpers import load_resource

up_textures = [
    load_resource("player/up0.png"),
    load_resource("player/up1.png"),
]

right_textures = [
    load_resource("player/right0.png"),
    load_resource("player/right1.png"),
]

down_textures = [
    load_resource("player/down0.png"),
    load_resource("player/down1.png"),
]

left_textures = [
    load_resource("player/left0.png"),
    load_resource("player/left1.png"),
]


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

        match direction:
            case Direction.UP:
                self.texture = up_textures[0]
            case Direction.RIGHT:
                self.texture = right_textures[0]
            case Direction.DOWN:
                self.texture = down_textures[0]
            case Direction.LEFT:
                self.texture = left_textures[0]

    def remove_direction(self, direction: Direction):
        if self.second_wanted_direction == direction:
            self.second_wanted_direction = None
        elif self.wanted_direction == direction:
            self.wanted_direction = self.second_wanted_direction
            self.second_wanted_direction = None
        self.screenX: int = 0
        self.screenY: int = 0
