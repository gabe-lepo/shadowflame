import pygame as pg
from pygame.locals import *

from globals import *
from player import Player
from colors import Colors

#Initialization
pg.init()
display_info = pg.display.Info()
current_width, current_height = display_info.current_w, display_info.current_h
#screen = pg.display.set_mode((current_width, current_height), pg.FULLSCREEN)
screen = pg.display.set_mode((WIDTH, HEIGHT))

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
   
   screen.fill(colors.BLACK)
   #vert grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pg.draw.line(screen, (255, 255, 255), (current_width * (_/GRID_DEPTH), 0), (current_width * (_/GRID_DEPTH), current_height))
   #horiz grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pg.draw.line(screen, (255, 255, 255), (0, current_height * (_/GRID_DEPTH)), (current_width, current_height * (_/GRID_DEPTH)))

   screen.blit(p1.surface, p1.center_coord)

   pg.display.update()

pg.quit()
