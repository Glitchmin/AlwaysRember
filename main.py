import pygame
from Logic.Camera import Camera, CameraMode
from pygame.color import Color

from Logic.Camera import CameraMode
from Logic.Player import Player
from Logic.Direction import Direction

from Logic.TileSet import TileSet

SCREEN_WIDTH = 720  # px
SCREEN_HEIGHT = 720  # px
TILE_SIZE = 64  # px

TILEMAP_SIZE = 32

pygame.init()
pygame.font.init()
default_font = pygame.font.SysFont("Comic Sans MS", 15)
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
light = pygame.image.load('textures/square.png')

running = True

player_x = TILEMAP_SIZE // 2
player_y = TILEMAP_SIZE // 2

camera = Camera(screen, SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)

camera_x = SCREEN_WIDTH // 2 + (SCREEN_WIDTH / 2)
camera_y = SCREEN_HEIGHT // 2 + (SCREEN_HEIGHT / 2)
camera_step_x = (SCREEN_WIDTH // TILEMAP_SIZE) / 4
camera_step_y = (SCREEN_HEIGHT // TILEMAP_SIZE) / 4

camera_mode = CameraMode.Free

player = Player(100, player_x, player_y, pygame.image.load(open("textures/player.png")))

tileset = TileSet.generate(TILEMAP_SIZE, player)
tileset.tiles[player.position[0]][player.position[1]].npc = player
tileset.update_path()

def act():
    key_pressed = pygame.key.get_pressed()
    if camera.mode == CameraMode.Free:
        if key_pressed[pygame.K_a]:
            camera.x -= camera.step_x
        elif key_pressed[pygame.K_d]:
            camera.x += camera.step_x
        if key_pressed[pygame.K_w]:
            camera.y -= camera.step_y
        elif key_pressed[pygame.K_s]:
            camera.y += camera.step_y
    else:
        camera.x = (player.position[0] * TILE_SIZE) - (SCREEN_WIDTH / 2)
        camera.y = (player.position[1] * TILE_SIZE) - (SCREEN_HEIGHT / 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    tileset.move_npc(Direction.LEFT, player)
                    tileset.update_path()
                case pygame.K_RIGHT:
                    tileset.move_npc(Direction.RIGHT, player)
                    tileset.update_path()
                case pygame.K_UP:
                    tileset.move_npc(Direction.UP, player)
                    tileset.update_path()
                case pygame.K_DOWN:
                    tileset.move_npc(Direction.DOWN, player)
                    tileset.update_path()
                case pygame.K_c:
                    camera.mode = CameraMode.toggle(camera.mode)
                case _:
                    pass

        print(f"player pos: {player.position}, camera pos: ({camera.x}, {camera.y})")

    tileset.move_enemies()

def render():
    camera.clear()
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # draw ground texture
    for i in range(len(tileset.tiles)):
        for j in range(len(tileset.tiles[i])):

            # draw terrain
            tile = tileset.tiles[i][j]
            camera.render(tile.tileType.texture, i, j)
            screen.blit(
                tile.tileType.texture,
                ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y),
            )
            light.set_alpha(196)
            screen.blit(
                light,
                ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y),
            )

            # draw any game objects that are in this tile
            if tile.npc:
                camera.render(tile.npc.texture, i, j)

            # draw number of tile (for debugging)
            text_surface = default_font.render(f"({i},{j})", False, (0, 0, 0))
            camera.render(text_surface, i, j)

            screen.blit(
                text_surface, ((TILE_SIZE * i) - camera_x, (TILE_SIZE * j) - camera_y)
            )
    pygame.display.flip()

while running:
    act()
    render()


pygame.quit()
