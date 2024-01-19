import os

N = 0.2  # Степень рандомности и количество преград
SIZE_CELL = 60
FPS = 7
COLS, ROWS = 16, 16
START = (0, 0)
GOAL = (COLS - 1, ROWS - 1)
COLORS = {
    'WHITE': 'white',
    'ORANGE': 'darkorange',
    'GREEN': 'forestgreen',
    'GRAY': 'darkslategray',
    'BLUE': 'blue',
    'MAGENTA': 'magenta',
    'PURPLE': 'purple',
    'BROWN': 'brown',
    'BLACK': 'black'
}
WHITE, ORANGE, GREEN, GRAY, BLUE, MAGENTA, PURPLE, BROWN, BLACK = ['white', 'darkorange', 'forestgreen', \
                                                                   'darkslategray', 'blue', 'magenta', 'purple',
                                                                   'brown', 'black']

COLOR_COST = {0: (255, 255, 255), 1: (190, 190, 190), 2: (127, 127, 127), 3: (63, 63, 63), 4: (0, 0, 0)}

IMG = os.path.dirname(__file__)  # Полный путь к файлу

FONT = ('arial', 58)

SIZE_FONT = 75

SHIFT_BUTTON = 120
