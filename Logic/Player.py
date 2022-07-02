from Logic.Direction import Direction

from Logic.AbstractNPC import AbstractNPC
from  Logic.Item import AbstractItem, Weapon, LightSource, Items

from helpers import load_resource, load_texture


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
            load_texture("player.png"),
        )
        self.left_hand: LightSource | None = Items.torch
        self.right_hand: Weapon | None = Items.axe
        self.back_hand: AbstractItem | None = None
        self.screen_x: int = 0
        self.screen_y: int = 0
        self.wanted_direction: Direction | None = None
        self.second_wanted_direction: Direction | None = None

        self.up_textures = [
            load_resource("player/up0.png"),
            load_resource("player/up1.png"),
        ]

        self.right_textures = [
            load_resource("player/right0.png"),
            load_resource("player/right1.png"),
        ]

        self.down_textures = [
            load_resource("player/down0.png"),
            load_resource("player/down1.png"),
        ]

        self.left_textures = [
            load_resource("player/left0.png"),
            load_resource("player/left1.png"),
        ]

    def set_wanted_direction(self, direction: Direction):
        self.second_wanted_direction = self.wanted_direction
        self.wanted_direction = direction

        match direction:
            case Direction.UP:
                self.texture = self.up_textures[0]
            case Direction.RIGHT:
                self.texture = self.right_textures[0]
            case Direction.DOWN:
                self.texture = self.down_textures[0]
            case Direction.LEFT:
                self.texture = self.left_textures[0]

    def remove_direction(self, direction: Direction):
        if self.second_wanted_direction == direction:
            self.second_wanted_direction = None
        elif self.wanted_direction == direction:
            self.wanted_direction = self.second_wanted_direction
            self.second_wanted_direction = None
        self.screen_x: int = 0
        self.screen_y: int = 0
