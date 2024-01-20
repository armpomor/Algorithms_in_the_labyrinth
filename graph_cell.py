import logging
from random import random, randrange

import pygame as pg

from config import COLS, ROWS, START, GOAL, SIZE_CELL, COLORS, COLOR_COST, IMG, N

logger = logging.getLogger(__name__)


class Graph:
    def __init__(self) -> None:
        self.graph = {}  # Граф без весов, но со стенами (единицами)
        self.graph_cost = {}  # Граф с весами
        self.cols = COLS
        self.rows = ROWS
        self.grid = self.make_grid()
        self.grid_cost = self.make_grid_cost()

    def __repr__(self) -> str:
        return repr(self.graph)

    def make_grid(self) -> list[list[int]]:
        """
        Делаем сетку со стенами
        """
        self.grid = [[1 if random() < N else 0 for col in range(self.cols)] for row in range(self.rows)]
        self.grid[START[0]][START[1]] = 0  # Делаем стартовую и целевую 
        self.grid[GOAL[0]][GOAL[1]] = 0  # клетки нулевыми
        return self.grid

    def make_grid_cost(self) -> list[list[int]]:
        """
        Делаем сетку с весами
        """
        self.grid_cost = [[randrange(0, 5) for col in range(self.cols)] for row in range(self.rows)]
        return self.grid_cost

    def add_edges(self) -> dict[tuple[int, int], list[tuple[int, int]]]:
        """
        Добавляем ребра для лабиринта со стенами
        """
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if not col:
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.neighbours(x, y)[0]
        logger.debug(self.graph)  ########################################################################

        return self.graph

    def add_edges_cost(self) -> dict[tuple[int, int], list[tuple[int, tuple[int, int]]]]:
        """
        Добавляем ребра для лабиринта с весами
        """
        for y, row in enumerate(self.grid_cost):
            for x, col in enumerate(row):
                self.graph_cost[(x, y)] = self.graph_cost.get((x, y), []) + self.neighbours(x, y)[1]
        logger.debug(self.graph_cost)  ########################################################################
        return self.graph_cost

    def neighbours(self, x: int, y: int) -> tuple[list[tuple[int, int]], list[tuple[int, tuple[int, int]]]]:
        """
        Соседи
        """
        direct = [0, 1], [0, -1], [1, 0], [-1, 0]

        return [(x + dx, y + dy) for dx, dy in direct if self.neighbors_walls(x + dx, y + dy)], \
            [(self.grid_cost[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in direct if
             self.neighbors_scales(x + dx, y + dy)]

    def neighbors_scales(self, x: int, y: int) -> bool:
        """
        Соседи для лабиринта с весами
        """
        return True if 0 <= x < self.cols and 0 <= y < self.rows else False

    def neighbors_walls(self, x: int, y: int) -> bool:
        """
        Соседи для лабиринта со стенами
        """
        return True if 0 <= x < self.cols and 0 <= y < self.rows and not self.grid[y][x] else False


g = Graph()
graph = g.add_edges()
grid = g.grid
graph_cost = g.add_edges_cost()
grid_cost = g.grid_cost


class Cell(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, color=COLORS['WHITE']) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((SIZE_CELL - 2, SIZE_CELL - 2))
        self.image.fill(pg.Color(color))
        self.rect = pg.Rect(x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL - 2, SIZE_CELL - 2)
        self.circle = x * SIZE_CELL + SIZE_CELL // 2, y * SIZE_CELL + SIZE_CELL // 2
        self.radius = SIZE_CELL // 4
        self.radius2 = SIZE_CELL // 3

    @staticmethod
    def cell_cost() -> pg.sprite.Group:
        """
        Веса
        """
        cells_cost = pg.sprite.Group()
        for y, row in enumerate(grid_cost):
            for x, col in enumerate(row):
                cell = Cell(x, y, COLOR_COST[grid_cost[y][x]])
                cells_cost.add(cell)
        return cells_cost


class Obstruction(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, filename=f'{IMG}/image/6.png') -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert()
        self.image = pg.transform.scale(self.image, (SIZE_CELL - 2, SIZE_CELL - 2))
        self.rect = self.image.get_rect(topleft=(x * SIZE_CELL, y * SIZE_CELL))

    @staticmethod
    def cell_wall() -> pg.sprite.Group:
        """
        Стены
        """
        cells_wall = pg.sprite.Group()
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col:
                    cell = Obstruction(x, y, f'{IMG}/image/6.png')
                    cells_wall.add(cell)
        return cells_wall
