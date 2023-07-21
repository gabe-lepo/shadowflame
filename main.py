import pygame
from pygame.locals import *

from globals import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == KEYDOWN:
         if event.key == K_ESCAPE:
            running = False
   
   pygame.draw.circle(screen, (255, 0, 0), (250, 250), 50)

pygame.quit()
