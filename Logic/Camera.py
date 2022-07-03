from enum import Enum

import pygame as pygame


class CameraMode(Enum):
    Free = 0
    Follow = 1


class Camera:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        screen_width: int,
        screen_height: int,
        tilemap_size: int,
        initial_offset: tuple[int, int],
        mode: CameraMode = CameraMode.Free,
    ):
        self.__screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tilemap_size = tilemap_size
        self.mode = mode
        self.x = initial_offset[0] - screen_width // 2
        self.y = initial_offset[1] - screen_height // 2
        self.step_x = (screen_width // tilemap_size)
        self.step_y = (screen_height // tilemap_size)

    def clear(self):
        self.__screen.fill((255, 255, 255))

    def toggle_mode(self):
         match self.mode:
            case CameraMode.Free:
                self.mode = CameraMode.Follow
            case CameraMode.Follow:
                self.mode = CameraMode.Free

    def render(self, texture: pygame.surface.Surface, x: int, y: int):
        dest = ((self.tilemap_size * x) - self.x, (self.tilemap_size * y) - self.y)
        self.__screen.blit(texture, dest)
