from Logic.AbstractNPC import AbstractNPC
from Logic.Direction import Direction
from Logic.Tile import TileType
from Logic.Tile import Tile
from Logic.Player import Player
import queue
import random


class TileSet:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.tiles: list[list[Tile]] = [
            [Tile(TileType.GROUND) for _ in range(height)] for _ in range(width)
        ]
        self.dist_to_player: list[list[int]] = [
            [float("inf") for _ in range(height)] for _ in range(width)
        ]

    def move_npc(self, dir: Direction, npc: AbstractNPC):
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

    @staticmethod
    def generate(size: int) -> "TileSet":
        tileset = TileSet(size, size)

        # add stones in some random locations
        for i in range(size):
            for j in range(size):
                if random.random() > 0.2:
                    continue

                tileset.tiles[i][j] = Tile(TileType.STONE)

        return tileset

    def inbounds(self, position: tuple[int, int]):
        return 0 < position[0] < self.width and 0 < position[1] < self.height

    def walkable(self, position: tuple[int, int]):
        return self.inbounds(position) and self.tiles[position[0]][position[1]].tileType.walkable and \
               self.tiles[position[0]][position[1]].npc is None

    def update_path(self, player: Player):
        q: queue = queue.Queue()
        q.put(player.position)
        self.dist_to_player: list[list[int]] = [
            [float("inf") for _ in range(self.height)] for _ in range(self.width)
        ]
        self.dist_to_player[player.position[0]][player.position[1]] = 0
        while not q.empty():
            position: tuple[int, int] = q.get()
            for direction in Direction:
                new_position: tuple[int, int] = (position[0] + direction[0], position[1] + direction[1])
                if self.walkable(new_position) and self.dist_to_player[new_position[0]][new_position[1]] > self.dist_to_player[position[0]][position[1]] + 1:
                    self.dist_to_player[new_position[0]][new_position[1]] = self.dist_to_player[position[0]][position[1]] + 1
                    q.put(new_position)

    def get_direction_to_player(self, position: tuple[int, int]) -> Direction:
        for direction in Direction:
            new_position: tuple[int, int] = (position[0] + direction[0], position[1] + direction[1])
            if self.dist_to_player[new_position[0]][new_position[1]] < self.dist_to_player[position[0]][position[1]]:
                return direction

        # TODO: return random direction

        return direction.LEFT
