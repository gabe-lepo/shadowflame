import pygame as pg
from pygame.locals import *

from globals import *
from player import Player
from colors import Colors
from app import App

#Initialization
app = App()
app.run()

# Setup objects
p1 = Player()
colors = Colors()

running = True
while running:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         running = False
      elif event.type == KEYDOWN:
         if event.key == K_ESCAPE:
            running = False
   
   app.main_screen.display.fill(colors.BLACK)
   #vert grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pg.draw.line(main_screen.display, (255, 255, 255), (current_width * (_/GRID_DEPTH), 0), (current_width * (_/GRID_DEPTH), current_height))
   #horiz grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pg.draw.line(main_screen.display, (255, 255, 255), (0, current_height * (_/GRID_DEPTH)), (current_width, current_height * (_/GRID_DEPTH)))

   app.main_screen.display.blit(p1.surface, p1.center_coord)

   app.main_screen.update()

pg.quit()
