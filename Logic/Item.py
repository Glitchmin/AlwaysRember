class AbstractItem:
    def __init__(self, name: str):
        self.name = name


class Weapon(AbstractItem):
    def __init__(self, name: str, damage: int, cooldown: float):
        super().__init__(name)
        self.damage = damage
        self.cooldown = cooldown


class LightSource(AbstractItem):
    def __init__(self, name: str, radius: float, angle: float):
        super().__init__(name)
        self.radius = radius
        self.angle = angle


Items = [
    Weapon("Crowbar", damage=1, cooldown=0.5),
    Weapon("Axe", damage=2, cooldown=1),
    LightSource("Torch", radius=2, angle=360),
    LightSource("Flashlight", radius=4, angle=60),
]
