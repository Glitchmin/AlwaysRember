from Logic.AbstractNPC import AbstractNPC
from Logic.Direction import Direction
from Logic.Enemy import Enemy, EnemyTypes
from Logic.Player import Player
from Logic.Tile import TileType
from Logic.Tile import Tile
import queue
import random


class TileSet:
    def __init__(self, width: int, height: int, player: Player):
        self.width: int = width
        self.height: int = height
        self.player = player
        self.tiles: list[list[Tile]] = [
            [Tile(TileType.GROUND) for _ in range(height)] for _ in range(width)
        ]
        self.enemies: list[Enemy] = []
        self.dist_to_player: list[list[int]] = [
            [1_000_000_000 for _ in range(height)] for _ in range(width)
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

    def addEnemy(self, enemy: Enemy):
        self.enemies.append(enemy)
        self.tiles[2][2].npc = enemy

    @staticmethod
    def generate(size: int, player: Player) -> "TileSet":
        tileset = TileSet(size, size, player)
        # add stones in some random locations
        for i in range(size):
            for j in range(size):
                if random.random() > 0.2:
                    continue

                tileset.tiles[i][j] = Tile(TileType.STONE)
        tileset.addEnemy(Enemy(2, 2, EnemyTypes.BABOL, player))
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
                print(f'{direction.value}')
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
        for direction in Direction:
            val = direction.value
            new_position: tuple[int, int] = (
                position[0] + val[0],
                position[1] + val[1],
            )
            if (
                self.dist_to_player[new_position[0]][new_position[1]]
                < self.dist_to_player[position[0]][position[1]]
            ):
                return direction

        # TODO: return random direction

        return Direction.LEFT
