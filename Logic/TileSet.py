import math
from math import acos

from pygame import mouse

from Logic.AbstractNPC import AbstractNPC
from Logic.Direction import Direction
from Logic.Enemy import Enemy, EnemyTypes
from Logic.Player import Player
from Logic.Tile import TileType
from Logic.Tile import Tile
import queue
import random


class TileSet:
    def __init__(self, width: int, height: int, player: Player, tile_size):
        self.width: int = width
        self.height: int = height
        self.player = player
        self.tile_size = tile_size
        self.tiles: list[list[Tile]] = [
            [Tile(TileType.GROUND) for _ in range(height)] for _ in range(width)
        ]
        self.enemies: list[Enemy] = []
        self.dist_to_player: list[list[int]] = [
            [1_000_000_000 for _ in range(height)] for _ in range(width)
        ]

    def update_times(self, elapsed_time: float):
        self.player.update_time(elapsed_time)
        for enemy in self.enemies:
            enemy.update_time(elapsed_time)

    def is_light(self, is_night: bool, x, y, camera_x, camera_y):
        angle = 0.0
        if not self.player.screenX - mouse.get_pos()[0] == 0:
            angle = math.atan((self.player.screenY - mouse.get_pos()[1]) / (self.player.screenX - mouse.get_pos()[0]))
            angle = math.degrees(angle)
        if self.player.screenX < mouse.get_pos()[0]:
            angle = angle + 90
        else:
            angle = angle + 270

        print("angle =", angle)

        angle_tile_player = 0.0
        tile_x = (x) * self.tile_size - camera_x
        tile_y = (y) * self.tile_size - camera_y
        if not self.player.screenX - tile_x == 0:
            angle_tile_player = math.atan((self.player.screenY - tile_y) / (self.player.screenX - tile_x))
            angle_tile_player = math.degrees(angle_tile_player)
        if self.player.screenX < tile_x:
            angle_tile_player = angle_tile_player + 90
        else:
            angle_tile_player = angle_tile_player + 270

        print("angle_tile_player =", angle_tile_player)

        if not is_night:
            return True
        else:
            return ((self.player.position[0] - x) ** 2 +
                    (self.player.position[1] - y) ** 2) <= self.player.leftHand.radius**2 and \
                   min(360-abs(angle_tile_player - angle),abs(angle_tile_player - angle)) <= self.player.leftHand.angle

    def move_enemies(self):
        for enemy in self.enemies:
            self.move_npc(self.get_direction_to_player(enemy.position), enemy)

    def move_npc(self, dir: Direction, npc: AbstractNPC):
        if npc.can_move():
            start_tile: Tile = self.tiles[npc.position[0]][npc.position[1]]
            final_tile: Tile = self.tiles[npc.position[0] + dir.value[0]][
                npc.position[1] + dir.value[1]
                ]
            if final_tile.npc is None and final_tile.tileType.walkable:
                final_tile.npc = npc
                start_tile.npc = None
                npc.move(dir)

    def get_tile(self, x: int, y: int):
        return self.tiles[x][y]

    def add_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)
        self.tiles[enemy.position[0]][enemy.position[1]].npc = enemy

    @staticmethod
    def generate(size: int, player: Player, tile_size: int) -> "TileSet":
        tileset = TileSet(size, size, player, tile_size)
        # add stones in some random locations
        for i in range(size):
            for j in range(size):
                if random.random() > 0.2:
                    continue

                tileset.tiles[i][j] = Tile(TileType.STONE)
        tileset.add_enemy(Enemy(2, 2, 0.5, EnemyTypes.BABOL, player))
        return tileset

    def inbounds(self, position: tuple[int, int]):
        return 0 < position[0] < self.width and 0 < position[1] < self.height

    def walkable(self, position: tuple[int, int]):
        return (
                self.inbounds(position)
                and self.tiles[position[0]][position[1]].tileType.walkable
                and self.tiles[position[0]][position[1]].npc is None
        )

    def update_path(self):
        q = queue.Queue()
        q.put(self.player.position)
        self.dist_to_player: list[list[int]] = [
            [float("inf") for _ in range(self.height)] for _ in range(self.width)
        ]
        self.dist_to_player[self.player.position[0]][self.player.position[1]] = 0
        while not q.empty():
            position: tuple[int, int] = q.get()
            for direction in Direction:
                val = direction.value
                new_position: tuple[int, int] = (
                    position[0] + val[0],
                    position[1] + val[1],
                )
                if (
                        self.walkable(new_position)
                        and self.dist_to_player[new_position[0]][new_position[1]]
                        > self.dist_to_player[position[0]][position[1]] + 1
                ):
                    self.dist_to_player[new_position[0]][new_position[1]] = (
                            self.dist_to_player[position[0]][position[1]] + 1
                    )
                    q.put(new_position)

    def get_direction_to_player(self, position: tuple[int, int]) -> Direction:
        result: Direction = Direction.LEFT
        best: int = 1_000_000_000
        for direction in Direction:
            val = direction.value
            new_position: tuple[int, int] = (
                position[0] + val[0],
                position[1] + val[1],
            )
            if (
                    self.dist_to_player[new_position[0]][new_position[1]]
                    < self.dist_to_player[position[0]][position[1]]
                    and self.dist_to_player[new_position[0]][new_position[1]] < best
            ):
                best = self.dist_to_player[new_position[0]][new_position[1]]
                result = direction

        # TODO: return random direction

        return result
