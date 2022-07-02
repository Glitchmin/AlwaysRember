import pygame as pygame

from helpers import load_resource

import random

class AbstractItem:
    def __init__(self, name: str, texture: pygame.surface.Surface):
        self.name = name
        self.texture = texture

    @classmethod
    def create_random(cls) -> "AbstractItem":
        return random.choice(Quests.quest_items)
        

class Weapon(AbstractItem):
    def __init__(
        self, name: str, texture: pygame.surface.Surface, damage: int, cooldown: float
    ):
        super().__init__(name, texture)
        self.damage = damage
        self.cooldown = cooldown


class LightSource(AbstractItem):
    def __init__(
        self, name: str, texture: pygame.surface.Surface, radius: float, angle: float
    ):
        super().__init__(name, texture)
        self.radius = radius
        self.angle = angle


class Quest(AbstractItem):
    def __init__(self, name: str, texture: pygame.surface.Surface):
        super().__init__(name, texture)


class Items:
    flashlight = LightSource(
        "flashlight",
        pygame.image.load(open("resources/czaszka0.png")),
        4.0,
        90,
    )

    torch = LightSource(
        "torch",
        load_resource("czaszka0.png"),
        4.0,
        90,
    )

    bone = Weapon(
        "Bone",
        load_resource("kosc0.png"),
        damage=1,
        cooldown=1,
    )

    axe = Weapon(
        "Axe",
        load_resource("kilof.png"),
        damage=2,
        cooldown=1,
    )

class Quests:
    sticks = Quest("Sticks ", load_resource("items/item0.png"))
    rubber = Quest("Rubber ", load_resource("items/item1.png"))
    pickaxe = Quest("Pickaxe ", load_resource("items/item2.png"))
    metal_scraps = Quest("Sticks, ", load_resource("items/item3.png"))
    radio = Quest("Sticks, ", load_resource("items/item4.png"))
    quest_items = [
        sticks,
        rubber,
        pickaxe,
        metal_scraps,
        radio,
    ]
