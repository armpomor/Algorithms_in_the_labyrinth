import pygame as pg

from config import COLS, SIZE_CELL, ROWS, START, COLORS
from graph_cell import Cell, graph


class DFS:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.graph = graph
        self.visited = ({START: None})
        self.stack = [START]
        self.vertex = START

    def dfs(self) -> None:
        if self.stack:
            self.vertex = self.stack.pop()

            for node in self.graph[self.vertex]:
                if node not in self.visited:
                    self.stack.append(node)
                    self.visited[node] = self.vertex

                    # draw dfs work
        [pg.draw.rect(self.screen, COLORS['GREEN'], Cell(x, y).rect) for x, y in self.visited]
        [pg.draw.rect(self.screen, COLORS['GRAY'], Cell(x, y).rect) for x, y in self.stack]

        # draw path
        path = self.vertex
        while path:
            pg.draw.rect(self.screen, COLORS['WHITE'], Cell(*path).rect, border_radius=SIZE_CELL // 3)
            path = self.visited[path]

        # draw start and head
        head = self.vertex
        pg.draw.rect(self.screen, COLORS['BLUE'], Cell(*START), border_radius=SIZE_CELL // 3)
        pg.draw.rect(self.screen, COLORS['MAGENTA'], Cell(*head), border_radius=SIZE_CELL // 3)
