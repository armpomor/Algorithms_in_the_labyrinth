from collections import deque

import pygame as pg

from config import COLORS, COLS, SIZE_CELL, ROWS, START
from graph_cell import graph, Cell


class BFS:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.graph = graph
        self.start = START
        self.queue = deque([self.start])
        self.visited = ({self.start: None})
        self.cur_node = self.start

    def bfs(self) -> None:

        if self.queue:
            self.cur_node = self.queue.popleft()
            next_nodes = self.graph[self.cur_node]

            for node in next_nodes:
                if node not in self.visited:
                    self.queue.append(node)
                    self.visited[node] = self.cur_node

        # draw BFS work
        [pg.draw.rect(self.screen, COLORS['GREEN'], Cell(x, y).rect) for x, y in self.visited]
        [pg.draw.rect(self.screen, COLORS['GRAY'], Cell(x, y).rect) for x, y in self.queue]

        # draw path
        head = path = self.cur_node
        while path:
            pg.draw.rect(self.screen, COLORS['WHITE'], Cell(*path).rect, border_radius=SIZE_CELL // 3)
            path = self.visited[path]

        # draw start and head 
        pg.draw.rect(self.screen, COLORS['BLUE'], Cell(*START), border_radius=SIZE_CELL // 3)
        pg.draw.rect(self.screen, COLORS['MAGENTA'], Cell(*head), border_radius=SIZE_CELL // 3)
