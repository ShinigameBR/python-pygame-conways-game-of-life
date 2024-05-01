import pygame as pg
import sys
from simulation import Simulation

BACKGROUND_COLOR = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 12

pg.init()

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(BACKGROUND_COLOR)
pg.display.set_caption("Game of Life")

clock = pg.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#Gameloop
while(True):
    
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    # Update
    simulation.update()
    
    # Draw
    simulation.draw(window)
    
    # Control
    pg.display.update()
    clock.tick(FPS)