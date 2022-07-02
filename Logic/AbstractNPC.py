from Logic.Direction import Direction

import pygame as pygame


class AbstractNPC:
    def __init__(
        self,
        hp: int,
        x: int,
        y: int,
        move_cooldown: float,
        texture: pygame.surface.Surface,
    ):
        self.__hp = hp
        self.__x = x
        self.__y = y
        self.__texture = texture
        self.__time = 0.0
        self.__move_cooldown = move_cooldown

    @property
    def hp(self):
        return self.__hp

    @property
    def position(self) -> tuple[int, int]:
        return self.__x, self.__y

    @property
    def texture(self) -> pygame.surface.Surface:
        return self.__texture

    def move(self, dir: Direction):
        self.__x += dir.value[0]
        self.__y += dir.value[1]

    def update_time(self, elapsed_time: float):
        self.__time += elapsed_time

    def can_move(self) -> bool:
        if self.__time >= self.__move_cooldown:
            self.__time = 0
            return True
        return False

    def getDamaged(self, damage: int):
        self.__hp -= damage
