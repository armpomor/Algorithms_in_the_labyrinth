from collections import deque
from graph_cell import graph, Cell
from config import *
import pygame as pg


class BFS:
    def __init__(self):
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.graph = graph
        self.start = START
        self.queue = deque([self.start])
        self.visited = ({self.start: None})
        self.cur_node = self.start

    def bfs(self):

        if self.queue:
            self.cur_node = self.queue.popleft()
            next_nodes = self.graph[self.cur_node]

            for node in next_nodes:
                if node not in self.visited:
                    self.queue.append(node)
                    self.visited[node] = self.cur_node

        # draw BFS work
        [pg.draw.rect(self.screen, GREEN, Cell(x, y).rect) for x, y in self.visited]
        [pg.draw.rect(self.screen, GRAY, Cell(x, y).rect) for x, y in self.queue]

        # draw path
        head = path = self.cur_node
        while path:
            pg.draw.rect(self.screen, WHITE, Cell(*path).rect, border_radius=SIZE_CELL // 3)
            path = self.visited[path]

        # draw start and head 
        pg.draw.rect(self.screen, BLUE, Cell(*START), border_radius=SIZE_CELL // 3)
        pg.draw.rect(self.screen, MAGENTA, Cell(*head), border_radius=SIZE_CELL // 3)
