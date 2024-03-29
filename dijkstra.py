from heapq import heappush, heappop

import pygame as pg

from config import COLS, SIZE_CELL, ROWS, START, COLORS, GOAL
from graph_cell import Cell, graph_cost


class Dijkstra:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.graph = graph_cost
        self.queue = []
        self.cost_visited = {START: 0}
        self.visited = {START: None}
        heappush(self.queue, (0, START))
        self.cur_node = None

    def dijkstra(self) -> None:
        # draw work
        [pg.draw.circle(self.screen, COLORS['GREEN'], Cell(x, y).circle, Cell().radius) for x, y in self.visited]
        [pg.draw.circle(self.screen, COLORS['ORANGE'], Cell(*xy).circle, Cell().radius) for _, xy in self.queue]

        # finish
        pg.draw.rect(self.screen, COLORS['PURPLE'], Cell(*GOAL).rect, border_radius=SIZE_CELL // 3)
        # logic
        if self.queue:
            cur_cost, self.cur_node = heappop(self.queue)
            if self.cur_node == GOAL:
                self.queue = []
                pass

            next_nodes = self.graph[self.cur_node]
            for node in next_nodes:
                neigh_cost, neigh_node = node
                new_cost = self.cost_visited[self.cur_node] + neigh_cost

                if neigh_node not in self.cost_visited or new_cost < self.cost_visited[neigh_node]:
                    heappush(self.queue, (new_cost, neigh_node))
                    self.cost_visited[neigh_node] = new_cost
                    self.visited[neigh_node] = self.cur_node

        # draw path
        head, path = self.cur_node, self.cur_node
        while path:
            pg.draw.circle(self.screen, COLORS['BROWN'], Cell(*path).circle, Cell().radius)
            path = self.visited[path]

        # draw start and head 
        pg.draw.rect(self.screen, COLORS['BLUE'], Cell(*START), border_radius=SIZE_CELL // 3)
        pg.draw.circle(self.screen, COLORS['MAGENTA'], Cell(*head).circle, Cell().radius2)
