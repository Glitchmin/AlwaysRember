import pygame
from Logic.Player import Player
from Logic.Direction import Direction

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720  # px
SCREEN_HEIGHT = 720  # px
TILE_SIZE = 64  # in pixels

TILEMAP_SIZE = 32

pygame.init()
pygame.font.init()
default_font = pygame.font.SysFont("Comic Sans MS", 15)
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

# TODO: create some init method

player_x = TILEMAP_SIZE // 2
player_y = TILEMAP_SIZE // 2

camera_x = SCREEN_WIDTH // 2 + (SCREEN_WIDTH / 2)
camera_y = SCREEN_HEIGHT // 2 + (SCREEN_HEIGHT / 2)
camera_step_x = (SCREEN_WIDTH // TILEMAP_SIZE) / 4
camera_step_y = (SCREEN_HEIGHT // TILEMAP_SIZE) / 4

player = Player(100, player_x, player_y, pygame.image.load(open("textures/player.png")))

tileset = TileSet.generate(TILEMAP_SIZE)
tileset.tiles[player.position[0]][player.position[1]].npc = player


while running:
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a]:
        camera_x -= camera_step_x
    elif key_pressed[pygame.K_d]:
        camera_x += camera_step_x
    if key_pressed[pygame.K_w]:
        camera_y -= camera_step_y
    elif key_pressed[pygame.K_s]:
        camera_y += camera_step_y
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    tileset.move_npc(Direction.LEFT, player)
                case pygame.K_RIGHT:
                    tileset.move_npc(Direction.RIGHT, player)
                case pygame.K_UP:
                    tileset.move_npc(Direction.UP, player)
                case pygame.K_DOWN:
                    tileset.move_npc(Direction.DOWN, player)
                case _:
                    pass

        print(f"player pos: {player.position}, camera pos: ({camera_x}, {camera_y})")

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tileset.tiles)):
        for j in range(len(tileset.tiles[i])):

            # draw terrain
            tile = tileset.tiles[i][j]
            screen.blit(
                tile.tileType.texture,
                ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y),
            )

            # draw any game objects that are in this tile
            if tile.npc:
                screen.blit(
                    tile.npc.texture,
                    ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y),
                )

            # draw number of tile (for debugging)
            text_surface = default_font.render(f"({i},{j})", False, (0, 0, 0))
            screen.blit(
                text_surface, ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y)
            )

    pygame.display.flip()

pygame.quit()
