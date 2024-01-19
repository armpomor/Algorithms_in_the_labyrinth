"""Программа Лабиринт демонстрирует действия следующих алгоритмов:
BFS, DFS, LEE, Dijkstra, A*. Чем выше вес клетки, тем она темнее на сетке с весами.
"""

import pygame as pg

from a_star import AStar
from bfs import BFS
from button import Button
from config import COLS, IMG, SIZE_CELL, ROWS, FPS, SIZE_FONT, SHIFT_BUTTON, COLORS
from dfs import DFS
from dijkstra import Dijkstra
from graph_cell import Cell, Obstruction
from lee import Lee


class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.clock = pg.time.Clock()
        self.background = pg.image.load(f"{IMG}/image/Background.png").convert()
        self.background = pg.transform.scale(self.background, (COLS * SIZE_CELL, ROWS * SIZE_CELL))
        self.walls = Obstruction().cell_wall()  # Стены
        self.cost = Cell().cell_cost()  # Веса
        self.bfs = BFS()
        self.dfs = DFS()
        self.lee = Lee()
        self.dijkstra = Dijkstra()
        self.a_star = AStar()

    @staticmethod
    def exit() -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

    @staticmethod
    def get_font() -> pg.font.Font:
        return pg.font.Font(f'{IMG}/image/font_1.ttf', SIZE_FONT)

    @staticmethod
    def pos_button(index: int) -> tuple[int, int]:
        return COLS * SIZE_CELL / 2, ROWS * 10 + SHIFT_BUTTON * index

    def draw(self) -> None:
        pg.display.update()
        self.clock.tick(FPS)
        self.screen.fill(COLORS['BLACK'])

    def bfs_algorithim(self) -> None:
        while True:
            self.walls.draw(self.screen)
            self.bfs.bfs()
            self.draw()
            self.exit()

    def dfs_algorithim(self) -> None:
        while True:
            self.walls.draw(self.screen)
            self.dfs.dfs()
            self.draw()
            self.exit()

    def lee_algorithim(self) -> None:
        while True:
            self.walls.draw(self.screen)
            self.lee.num_step()
            self.lee.pave_path()
            self.draw()
            self.exit()

    def a_star_algorithim(self) -> None:
        while True:
            self.cost.draw(self.screen)
            self.a_star.a_star()
            self.draw()
            self.exit()

    def dijkstra_algorithim(self) -> None:
        while True:
            self.cost.draw(self.screen)
            self.dijkstra.dijkstra()
            self.draw()
            self.exit()

    def main_menu(self) -> None:
        pg.display.set_caption('Graph Algorithms')
        while True:
            self.screen.blit(self.background, (0, 0))

            mouse_pos = pg.mouse.get_pos()

            bfs_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(0),
                                text_input='BFS', font=self.get_font(), base_color=COLORS['BROWN'],
                                hovering_color=COLORS['WHITE'])
            dfs_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(1),
                                text_input='DFS', font=self.get_font(), base_color=COLORS['BROWN'],
                                hovering_color=COLORS['WHITE'])
            lee_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(2),
                                text_input='Lee', font=self.get_font(), base_color=COLORS['BROWN'],
                                hovering_color=COLORS['WHITE'])
            a_star_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(3),
                                   text_input='A*', font=self.get_font(), base_color=COLORS['BROWN'],
                                   hovering_color=COLORS['WHITE'])
            dijkstra_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(4),
                                     text_input='Dijkstra', font=self.get_font(), base_color=COLORS['BROWN'],
                                     hovering_color=COLORS['WHITE'])

            for button in [bfs_button, dfs_button, lee_button, a_star_button, dijkstra_button]:
                button.change_color(mouse_pos)
                button.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if bfs_button.check_for_input(mouse_pos):
                        self.bfs_algorithim()
                    if dfs_button.check_for_input(mouse_pos):
                        self.dfs_algorithim()
                    if lee_button.check_for_input(mouse_pos):
                        self.lee_algorithim()
                    if a_star_button.check_for_input(mouse_pos):
                        self.a_star_algorithim()
                    if dijkstra_button.check_for_input(mouse_pos):
                        self.dijkstra_algorithim()

            self.draw()


if __name__ == '__main__':
    app = App()
    app.main_menu()
