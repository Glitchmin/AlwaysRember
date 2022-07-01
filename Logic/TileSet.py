from textures.Logic.Tile import Tile


class TileSet:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.tiles: [[Tile]] = [[Tile(0) for _ in range(height)] for _ in range(width)]

    def get_tile(self, x: int, y: int):
        return self.tiles[x][y]
