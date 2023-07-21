import pygame as pg
from pygame.locals import *

from globals import *
from colors import Colors

class Player(pg.sprite.Sprite):
   def __init__(self):
      super(Player, self).__init__()
      colors = Colors()

      self.surface = pg.Surface((75, 25))
      self.center_coord = (
         (WIDTH - self.surface.get_width()) / 2,
         (HEIGHT - self.surface.get_height()) / 2
      )
      self.surface.fill(colors.RED)
      self.rect = self.surface.get_rect()