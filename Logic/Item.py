from enum import Enum


class AbstractItem:
    def __init__(self, name):
        self.name = name


class Weapon(AbstractItem):
    def __init__(self, name, dmg, cd):
        super().__init__(name)
        self.dmg = dmg
        self.cd = cd


class LightSource(AbstractItem):
    def __init__(self, name, radius, angle):
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
