import pygame
from pygame.locals import *

from colors import Colors

class Player(pygame.sprite.Sprite):
   def __init__(self):
      super(Player, self).__init__()
      colors = Colors()

      self.surface = pygame.Surface((75, 25))
      self.surface.fill(colors.RED)
      self.rect = self.surface.get_rect()