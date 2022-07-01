from Logic.AbstractNPC import AbstractNPC
from Logic.Direction import Direction
from Logic.Tile import TileType
from Logic.Tile import Tile
import random


class TileSet:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.tiles: list[list[Tile]] = [
            [Tile(TileType.GROUND) for _ in range(height)] for _ in range(width)
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
