import pygame
from Logic.Player import Player
from Logic.Direction import Direction

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

TILEMAP_SIZE = 12

pygame.init()
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

# TODO: create some init method

player_x = TILEMAP_SIZE // 2
player_y = TILEMAP_SIZE // 2

player = Player(100, player_x, player_y, pygame.image.load(open("textures/player.png")))

tileset = TileSet.generate(TILEMAP_SIZE)
tileset.tiles[player.getPosition()[0]][player.getPosition()[1]].npc = player


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"{event.key}")
            running = False

        if event.type == pygame.KEYDOWN:
            print(f"{event.key=}")

            match event.key:
                case pygame.K_LEFT:
                    tileset.move_npc( Direction.LEFT, player)
                case pygame.K_RIGHT:
                    tileset.move_npc(Direction.RIGHT, player)
                case pygame.K_UP:
                    tileset.move_npc(Direction.UP, player)
                case pygame.K_DOWN:
                    tileset.move_npc(Direction.DOWN, player)
                case _:
                    pass

        print(f"{player.getPosition()}")

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tileset.tiles)):
        for j in range(len(tileset.tiles[i])):
            tile = tileset.tiles[i][j]
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
                    (
                        texture.get_width() * i,
                        texture.get_height() * j,
                    ),
                )

    pygame.display.flip()

pygame.quit()
