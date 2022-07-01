import pygame
import random

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

TILEMAP_SIZE = 32

pygame.init()
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

ground_texture = pygame.image.load(open("textures/ground.png"))
stone_texture = pygame.image.load(open("textures/stone.png"))

def generate_map() -> TileSet:
    tilemap: list[list[pygame.Surface]] = []    

    # fill with default ground tiles
    for i in range(TILEMAP_SIZE):
        row: list[pygame.Surface] = []
        for j in range(TILEMAP_SIZE):
            row.append(ground_texture)
        
        tilemap.append(row)

    # add stones in some random locations
    for i in range(TILEMAP_SIZE):
        for j in range(TILEMAP_SIZE):
            if random.random() > 0.5:
                continue
        
            tilemap[i][j] = stone_texture

    return tilemap


tilemap = generate_map()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            texture = tilemap[i][j]
            screen.blit(texture,
                (
                    texture.get_width() * i,
                    texture.get_height() * j,
                ),
            )

    pygame.display.flip()

pygame.quit()
