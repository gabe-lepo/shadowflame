import pygame as pg
from pygame.locals import *

from globals import *
from screen import Screen
from player import Player

class App:
   def __init__(self):
      pg.init()
      self.main_screen = Screen(fullscreen=False)
      self.p1 = Player()
      self.clock = pg.time.Clock()
      self.running = True
   
   def run(self):
      while self.running:
         for event in pg.event.get():
            if event.type == pg.QUIT:
               self.running = False
            elif event.type == pg.KEYDOWN:
               if event.key == K_ESCAPE:
                  self.running = False
         
         self.main_screen.clear()
         self.main_screen.update()
