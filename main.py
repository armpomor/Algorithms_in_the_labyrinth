import pygame as pg
from config import *
from graph_cell import Cell, Obstruction
from bfs import BFS
from dfs import DFS
from lee import Lee
from dijkstra import Dijkstra
from A_star import A_star
from button import Button


"""Программа Лабиринт демонстрирует действия следующих алгоритмов:
BFS, DFS, LEE, Dijkstra, A*. Чем выше вес клетки, тем она темнее на сетке с весами.
"""


class App:
    def __init__(self):
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.clock = pg.time.Clock()
        self.background = pg.image.load(f"{IMG}/image/Background.png").convert()
        self.background = pg.transform.scale(self.background, (COLS * SIZE_CELL, ROWS * SIZE_CELL))
        self.walls = Obstruction().cell_wall()  # Стены
        self.cost = Cell().cell_cost()   # Веса
        self.bfs = BFS()
        self.dfs = DFS()
        self.lee = Lee()
        self.dijkstra = Dijkstra()
        self.a_star = A_star()
        

    def draw(self):
        pg.display.update()
        self.clock.tick(FPS)
        self.screen.fill(BLACK)
        
        
    def exit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit() 
            
            
    def bfs_algorithim(self):
        while True:
            self.walls.draw(self.screen)
            self.bfs.bfs()
            self.draw()
            self.exit()
            
            
    def dfs_algorithim(self):
        while True:
            self.walls.draw(self.screen)
            self.dfs.dfs()
            self.draw()
            self.exit()
            
            
    def lee_algorithim(self):
        while True:
            self.walls.draw(self.screen)
            self.lee.num_step()
            self.lee.pave_path()
            self.draw()
            self.exit()
            
            
    def a_star_algorithim(self):
        while True:
            self.cost.draw(self.screen)
            self.a_star.a_star()
            self.draw()
            self.exit()
            
            
    def dijkstra_algorithim(self):
        while True:
            self.cost.draw(self.screen)
            self.dijkstra.dijkstra()
            self.draw()
            self.exit()
            
            
    def get_font(self):
        return pg.font.Font(f'{IMG}/image/font_1.ttf', SIZE_FONT)
    
    
    def pos_button(self, index):
        return COLS * SIZE_CELL / 2, ROWS * 10 + SHIFT_BUTTON * index
        
                 
    def main_menu(self):
        pg.display.set_caption('Graph Algorithms')
        while True:
            self.screen.blit(self.background, (0, 0))
            
            mouse_pos = pg.mouse.get_pos()
            
            bfs_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(0), 
                                text_input='BFS', font=self.get_font(), base_color=BROWN, hovering_color=WHITE)
            dfs_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(1), 
                                text_input='DFS', font=self.get_font(), base_color=BROWN, hovering_color=WHITE)
            lee_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(2), 
                                text_input='Lee', font=self.get_font(), base_color=BROWN, hovering_color=WHITE)
            a_star_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(3), 
                                text_input='A*', font=self.get_font(), base_color=BROWN, hovering_color=WHITE)
            dijkstra_button = Button(image=pg.image.load(f'{IMG}/image/0.png'), pos=self.pos_button(4), 
                                text_input='Dijkstra', font=self.get_font(), base_color=BROWN, hovering_color=WHITE)
            
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
