import pygame as pg
from pygame.locals import *

from globals import *
from screen import Screen

class App():
   def __init__(self) -> None:
      pg.init()
      self.screen = Screen()
