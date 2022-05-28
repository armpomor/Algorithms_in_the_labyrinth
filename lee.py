from config import *
import pygame as pg
from graph_cell import Cell, grid


"""Создаём нулевую матрицу подходящего размера.
Ставим 1 в точку старта.
Во все позиции вокруг 1 ставим 2 , если нет стены.
Вокруг двоек ставим тройки ( 3). Тоже, если нет стены.
И так далее…
Как только ставим цифру в точку финиша, останавливаемся. Это число и является минимальной длиной пути."""


pg.init()


class Lee:
    def __init__(self):
        self.screen = pg.display.set_mode([COLS * SIZE_CELL, ROWS * SIZE_CELL])
        self.matrix_zero = [[0 for x in range(COLS)] for y in range(ROWS)]
        self.step = 0
        self.path = [GOAL]
        self.number = pg.font.SysFont(*FONT)
        
        
    def make_step(self):
        """Метод принимает число шагов step в качестве аргумента.
        Сканирует матрицу при помощи цикла for.
        Если находится число, которое соответствует количеству шагов step, 
        смотрим на ячейки вокруг и проверяем:
        1. Нет ли здесь пока еще числа.
        2. Нет ли здесь стены.
        И ставим step+1 этим ячейкам."""
        self.matrix_zero[START[0]][START[1]] = 1
        
        pg.draw.rect(self.screen, BLUE, Cell(*START).rect) # draw start
        sc_text = self.number.render(str(1), 1, WHITE) # draw number start
        self.screen.blit(sc_text, (0, 0))
        
        for i, _ in enumerate(self.matrix_zero):
            for j, _ in enumerate(self.matrix_zero[i]):
                if self.matrix_zero[i][j] == self.step:
                    if i > 0 and self.matrix_zero[i - 1][j] == 0 and grid[i - 1][j] == 0:
                        self.matrix_zero[i - 1][j] = self.step + 1
                       
                        pg.draw.rect(self.screen, GREEN, Cell(i - 1, j).rect)
                        
                        sc_text = self.number.render(str(self.step + 1), 1, WHITE)
                        self.screen.blit(sc_text, (i * SIZE_CELL - SIZE_CELL, j * SIZE_CELL))
                       
                    if j > 0 and self.matrix_zero[i][j - 1] == 0 and grid[i][j - 1] == 0:
                        self.matrix_zero[i][j - 1] = self.step + 1
                        
                        pg.draw.rect(self.screen, GREEN, Cell(i, j - 1).rect)
                        
                        sc_text = self.number.render(str(self.step + 1), 1, WHITE)
                        self.screen.blit(sc_text, (i * SIZE_CELL, j * SIZE_CELL - SIZE_CELL))
                        
                    if i < len(grid) - 1 and self.matrix_zero[i + 1][j] == 0 and grid[i + 1][j] == 0:
                        self.matrix_zero[i + 1][j] = self.step + 1
                        
                        pg.draw.rect(self.screen, GREEN, Cell(i + 1, j).rect)
                        
                        sc_text = self.number.render(str(self.step + 1), 1, WHITE)
                        self.screen.blit(sc_text, (i * SIZE_CELL + SIZE_CELL, j * SIZE_CELL))
                        
                    if j < len(grid[i]) - 1 and self.matrix_zero[i][j + 1] == 0 and grid[i][j + 1] == 0:
                        self.matrix_zero[i][j + 1] = self.step + 1
                        
                        pg.draw.rect(self.screen, GREEN, Cell(i, j + 1).rect)
                        
                        sc_text = self.number.render(str(self.step + 1), 1, WHITE)
                        self.screen.blit(sc_text, (i * SIZE_CELL, j * SIZE_CELL + SIZE_CELL))
                        
                        
    def num_step(self):
        if self.matrix_zero[GOAL[0]][GOAL[1]] == 0:
            self.step += 1
            self.make_step()
            
            
    def pave_path(self):
        """Задача теперь — найти кратчайший путь по этой матрице.
        Шаги для решения следующие:
        Пойти в точку финиша, допустим, число здесь — finish.
        Найти соседнюю ячейку со значением finish - 1 , пойти туда, уменьшить finish на единицу.
        Повторить предыдущий шаг, пока не доберемся до начальной точки, а именно: finish = 1."""
        
        i, j = GOAL
        
        pg.draw.rect(self.screen, MAGENTA, Cell(*GOAL), border_radius=SIZE_CELL // 3)
        
        finish = self.matrix_zero[i][j]
        while finish > 1:
            if i > 0 and self.matrix_zero[i - 1][j] == finish - 1:
                i, j = i - 1, j
                self.path.append((i, j))
                
                pg.draw.rect(self.screen, WHITE, Cell(j, i).rect, border_radius=SIZE_CELL // 3)  
                finish -= 1
            elif j > 0 and self.matrix_zero[i][j - 1] == finish - 1:
                i, j = i, j - 1
                self.path.append((i, j))
                
                pg.draw.rect(self.screen, WHITE, Cell(j, i).rect, border_radius=SIZE_CELL // 3)
                finish -= 1
            elif i < len(grid) - 1 and self.matrix_zero[i + 1][j] == finish - 1:
                i, j = i + 1, j
                self.path.append((i, j))
                
                pg.draw.rect(self.screen, WHITE, Cell(j, i).rect, border_radius=SIZE_CELL // 3)
                finish -= 1
            elif j < len(grid[i]) - 1 and self.matrix_zero[i][j + 1] == finish - 1:
                i, j = i, j + 1
                self.path.append((i, j))
                
                pg.draw.rect(self.screen, WHITE, Cell(j, i).rect, border_radius=SIZE_CELL // 3)
                finish -= 1
                
            pg.draw.rect(self.screen, BLUE, Cell(*START).rect) # draw start
            
        self.path = list(reversed(self.path))
       
