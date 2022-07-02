import pygame as pygame


def load_resource(path: str) -> pygame.surface.Surface:
    return pygame.image.load(open(f"resources/{path}"))
