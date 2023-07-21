import pygame as pg

from globals import *

class Screen():
   def __init__(self, fullscreen: bool) -> None:
      if fullscreen:
         self.display = pg.display.set_mode((pg.display.Info().current_w, pg.display.Info().current_h), pg.FULLSCREEN)
      else:
         self.display = pg.display.set_mode((WIDTH, HEIGHT))
      pg.display.set_caption("Shadowflame")
   
   def clear(self):
      self.display.fill(BLACK)
   
   def update(self):
      pg.display.update()
