from enum import Enum

import pygame as pygame


class CameraMode(Enum):
    Free = 0
    Follow = 1

    @staticmethod
    def toggle(current: "CameraMode"):
        match current:
            case CameraMode.Free:
                return CameraMode.Follow
            case CameraMode.Follow:
                return CameraMode.Free


class Camera:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        screen_width: int,
        screen_height: int,
        tilemap_size: int,
        mode: CameraMode = CameraMode.Free,
    ):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tilemap_size = tilemap_size
        self.mode = mode
        self.x = screen_width // 2 + (screen_width // 2)
        self.y = screen_height // 2 + (screen_height // 2)
        self.step_x = (screen_width // tilemap_size) // 4
        self.step_y = (screen_height // tilemap_size) // 4

    def clear(self):
        self.screen.fill((255, 255, 255))

    def render(self, texture: pygame.surface.Surface, x: int, y: int):
        dest = ((self.tilemap_size * x) - self.x, (self.tilemap_size * y) - self.y)
        self.screen.blit(texture, dest)
