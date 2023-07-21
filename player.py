import pygame
from pygame.locals import *

from globals import *
from colors import Colors

class Player(pygame.sprite.Sprite):
   def __init__(self):
      super(Player, self).__init__()
      colors = Colors()

      self.surface = pygame.Surface((75, 25))
      self.center_coord = (
         (WIDTH - self.surface.get_width()) / 2,
         (HEIGHT - self.surface.get_height()) / 2
      )
      self.surface.fill(colors.RED)
      self.rect = self.surface.get_rect()