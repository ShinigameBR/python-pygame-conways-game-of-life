import pygame as pg
import sys
from simulation import Simulation
from events import event_management
from definitions import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, BACKGROUND_COLOR, CELL_SIZE

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
        else:
            event_management(simulation, event)

    # Update
    simulation.update()
    
    # Draw
    simulation.draw(window)
    
    # Control
    pg.display.update()
    clock.tick(FPS)