import pygame

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

TILEMAP_SIZE = 32

pygame.init()
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True


tilemap = TileSet.generate(TILEMAP_SIZE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tilemap.tiles)):
        for j in range(len(tilemap.tiles[i])):
            texture = tilemap.tiles[i][j].tileType.get_texture()
            screen.blit(
                texture,
                (
                    texture.get_width() * i,
                    texture.get_height() * j,
                ),
            )

    pygame.display.flip()

pygame.quit()
