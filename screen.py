import pygame as pg
from pygame.locals import *

from globals import *

class Screen():
   def __init__(self, fullscreen: bool):
      if fullscreen:
         self.display_info = pg.display.Info()
         self.fullscreen_width, self.fullscreen_height = self.display_info.current_w, self.display_info.current_h
         self.display = pg.display.set_mode((self.fullscreen_width, self.fullscreen_height), pg.FULLSCREEN)
      else:
         self.display = pg.display.set_mode((WIDTH, HEIGHT))
   
   def update(self):
      pg.display.update()
