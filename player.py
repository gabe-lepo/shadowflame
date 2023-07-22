import pygame as pg
from pygame.locals import *

class Player():
   def __init__(self) -> None:
      self.health = 100
   
   def check_dead(self):
      if self.health == 0:
         #do stuff
         self.health = 100
