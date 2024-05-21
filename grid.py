import pygame as pg
from random import choice
from definitions import CHOICE_RATE, LIVE_CELL_COLOR, DEAD_CELL_COLOR
class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for col in range(self.columns)] for row in range(self.rows)]
        
    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                color = LIVE_CELL_COLOR if self.cells[row][column] else DEAD_CELL_COLOR
                pg.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
    
    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = choice(CHOICE_RATE)
                
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0

    def toggle_cell(self, row: int, column: int):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]
        