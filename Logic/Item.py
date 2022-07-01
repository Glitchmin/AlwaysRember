from enum import Enum


class AbstractItem:
    def __init__(self, name: str):
        self.name = name


class Weapon(AbstractItem):
    def __init__(self, name: str, damage: int, cooldown: float):
        super().__init__(name)
        self.dmg = damage
        self.cooldown = cooldown


class LightSource(AbstractItem):
    def __init__(self, name: str, radius: float, angle: float):
        super().__init__(name)
        self.radius = radius
        self.angle = angle


ItemTab = [
    Weapon("Crowbar", 1, 0.5),
    LightSource("torch", 2, 360),
]


class Item(Enum):
    CROWBAR = 0
    TORCH = 1
