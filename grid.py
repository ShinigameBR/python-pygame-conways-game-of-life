import pygame as pg
from random import choice
class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for col in range(self.columns)] for row in range(self.rows)]
        
    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                pg.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
    
    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = choice([1, 0, 0, 0])