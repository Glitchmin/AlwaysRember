import pygame as pygame


class AbstractItem:
    def __init__(self, name: str, texture: pygame.surface.Surface):
        self.name = name
        self.texture = texture


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

flashlight = LightSource(
    "flashlight",
    pygame.image.load(open("resources/czaszka0.png")),
    4.0,
    90,
)

torch = LightSource(
    "torch",
    pygame.image.load(open("resources/torcz0.png")),
    4.0,
    180,
)

bone = Weapon(
    "Bone",
    pygame.image.load(open("resources/kosc0.png")),
    damage=1,
    cooldown=1,
)

axe = Weapon(
    "Axe",
    pygame.image.load(open("resources/kilof.png")),
    damage=2,
    cooldown=1,
)

sticks = Quest("Sticks ", pygame.image.load(open("resources/opona0.png")))
rubber = Quest("Rubber ", pygame.image.load(open("resources/opona0.png")))
pickaxe = Quest("Pickaxe ", pygame.image.load(open("resources/opona1.png")))
metal_scraps = Quest("Sticks, ", pygame.image.load(open("resources/opona0.png")))
radio = Quest("Sticks, ", pygame.image.load(open("resources/opona0.png")))

quest_items = [sticks, rubber, pickaxe, metal_scraps, radio]

# torch = (LightSource("Torch", radius=2, angle=360),)
# flashlight = (LightSource("Flashlight", radius=4, angle=60),)


items = [torch, bone, axe]
