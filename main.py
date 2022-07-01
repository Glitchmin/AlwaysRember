import pygame
from Logic.Player import Player
from Logic.Direction import Direction

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

TILEMAP_SIZE = 32

pygame.init()
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True


tilemap = TileSet.generate(TILEMAP_SIZE)


player_x = TILEMAP_SIZE // 2
player_y = TILEMAP_SIZE // 2

player = Player(100, player_x, player_y, pygame.image.load(open("textures/player.png")))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"{event.key}")
            running = False

        if event.type == pygame.KEYDOWN:
            print(f"{event.key=}")

            match event.key:
                case pygame.K_LEFT:
                    player.move(Direction.LEFT)
                case pygame.K_RIGHT:
                    player.move(Direction.RIGHT)
                case _:
                    pass

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tilemap.tiles)):
        for j in range(len(tilemap.tiles[i])):
            tile = tilemap.tiles[i][j]
            texture = tile.tileType.texture
            screen.blit(
                texture,
                (
                    texture.get_width() * i,
                    texture.get_height() * j,
                ),
            )
            if tile.npc:
                screen.blit(
                    tile.npc.getTexture(),
                    tile.npc.getPosition(),
                )

    tilemap.tiles[player.getPosition()[0]][player.getPosition()[1]].npc = player

    pygame.display.flip()

pygame.quit()
