import pygame
from game import Game

SCREEN_WIDTH = 720  # px
SCREEN_HEIGHT = 720  # px
TILE_SIZE = 64  # px
MAP_SIZE = 32  # tiles

pygame.init()
pygame.font.init()
default_font = pygame.font.SysFont("Comic Sans MS", 15)
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], vsync=1)


game = Game(
    screen,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TILE_SIZE,
    MAP_SIZE,
    default_font,
)

game.run()
