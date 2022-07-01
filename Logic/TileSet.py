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

    def get_tile(self, x: int, y: int):
        return self.tiles[x][y]

    @staticmethod
    def generate(size: int) -> "TileSet":
        tileset = TileSet(size, size)

        # add stones in some random locations
        for i in range(size):
            for j in range(size):
                if random.random() > 0.5:
                    continue

                tileset.tiles[i][j] = Tile(TileType.STONE)

        return tileset
