import pygame as pg
from simulation import Simulation
from definitions import CELL_SIZE

def event_management(simulation: Simulation, event: pg.event):
    
    if event.type == pg.MOUSEBUTTONDOWN:
        pos = pg.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        column = pos[0] // CELL_SIZE
        simulation.toggle_cell(row, column)
    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
            if simulation.status:
                simulation.stop()
                pg.display.set_caption("Game of Life - Stopped")
            else:
                simulation.start()
                pg.display.set_caption("Game of Life - Running")
        elif event.key == pg.K_UP:
            if FPS < 30:
                FPS += 2
        elif event.key == pg.K_DOWN:
            if FPS > 6:
                FPS -= 2
        elif event.key == pg.K_c:
            simulation.clear()
        elif event.key == pg.K_r:
            simulation.restart()