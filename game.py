import time
import pygame as pygame
from pygame import mouse
from pygame.surface import Surface

from Logic.Camera import Camera, CameraMode
from Logic.Direction import Direction
from Logic.Player import Player
from Logic.TileSet import TileSet


class Game:
    def __init__(
            self,
            screen: pygame.surface.Surface,
            screen_width: int,
            screen_height: int,
            tile_size: int,
            map_size: int,
            font: pygame.font.Font,
    ):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tile_size = tile_size
        self.map_size = map_size
        self.font = font
        self.black_square = pygame.image.load(open("textures/square.png"))

        self.running = True
        self.last_time = time.time()
        self.last_player_input = time.time()
        self.camera = Camera(screen, screen_width, screen_height, tile_size)
        self.player = Player(
            hp=100,
            x=map_size // 2,
            y=map_size // 2,
            move_cooldown=0.5,
            texture=pygame.image.load(open("textures/player.png")),
        )

        self.tileset = TileSet.generate(map_size, self.player, tile_size)
        self.tileset.tiles[self.player.position[0]][
            self.player.position[1]
        ].npc = self.player
        self.tileset.update_path()
        pass

    def run(self):
        while self.running:
            self.update_input()
            self.update()
            self.render()

        pygame.quit()

    def update_input(self):
        # get elapsed time
        current_time = time.time()
        elapsed_time, self.last_time = current_time - self.last_time, current_time

        self.tileset.update_times(elapsed_time)

        key_pressed = pygame.key.get_pressed()
        if self.camera.mode == CameraMode.Free:
            if key_pressed[pygame.K_a]:
                self.camera.x -= self.camera.step_x
            elif key_pressed[pygame.K_d]:
                self.camera.x += self.camera.step_x
            if key_pressed[pygame.K_w]:
                self.camera.y -= self.camera.step_y
            elif key_pressed[pygame.K_s]:
                self.camera.y += self.camera.step_y
        else:
            self.camera.x = (self.player.position[0] * self.tile_size) - (
                    self.screen_width / 2
            )
            self.camera.y = (self.player.position[1] * self.tile_size) - (
                    self.screen_height / 2
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        self.player.set_wanted_direction(Direction.LEFT)
                    case pygame.K_RIGHT:
                        self.player.set_wanted_direction(Direction.RIGHT)
                    case pygame.K_UP:
                        self.player.set_wanted_direction(Direction.UP)
                    case pygame.K_DOWN:
                        self.player.set_wanted_direction(Direction.DOWN)
                    case pygame.K_c:
                        self.camera.mode = CameraMode.toggle(self.camera.mode)
                    case _:
                        pass
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT:
                        self.player.remove_direction(Direction.LEFT)
                    case pygame.K_RIGHT:
                        self.player.remove_direction(Direction.RIGHT)
                    case pygame.K_UP:
                        self.player.remove_direction(Direction.UP)
                    case pygame.K_DOWN:
                        self.player.remove_direction(Direction.DOWN)

    def update(self):
        if self.player.wanted_direction is not None:
            self.tileset.move_npc(self.player.wanted_direction, self.player)

        print(
            f"player pos: {self.player.position}, camera pos: ({self.camera.x}, {self.camera.y})"
        )

        # move enemies
        self.tileset.update()

    def render(self):
        self.camera.clear()

        pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

        # draw ground texture
        for i in range(len(self.tileset.tiles)):
            for j in range(len(self.tileset.tiles[i])):

                # draw terrain
                tile = self.tileset.tiles[i][j]
                self.camera.render(tile.tileType.texture, i, j)

                #apply night
                self.black_square.set_alpha(255)
                if not self.tileset.is_light(True,i,j, self.camera.x, self.camera.y):
                    self.camera.render(self.black_square, i, j)

                # draw any game objects that are in this tile
                if tile.npc:
                    self.camera.render(tile.npc.texture, i, j)
                    if type(tile.npc) == Player:
                        self.player.screenX = self.camera.tilemap_size * (i+0.5) - self.camera.x
                        self.player.screenY = self.camera.tilemap_size * (j+0.5) - self.camera.y

                # draw number of tile (for debugging)
                text_surface = self.font.render(f"({i},{j})", False, (0, 0, 0))
                self.camera.render(text_surface, i, j)

        # draw UI
        self.draw_rect_with_border(
            50,
            self.screen_height - 100,
            width=100,
            height=50,
        )
        self.draw_rect_with_border(
            self.screen_width - 100,
            self.screen_height - 100,
            width=100,
            height=50,
        )

        pygame.display.flip()

    def draw_rect_with_border(self, x: int, y: int, width: int, height: int):
        pygame.draw.rect(self.screen, (127, 127, 127), (x, y, width, height), 0)
        for i in range(4):
            pygame.draw.rect(
                self.screen, (0, 0, 0), (x - i, y - i, width + 5, height + 5), 1
            )
