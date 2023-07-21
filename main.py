import pygame
from pygame.locals import *

from globals import *
from player import Player

#Initialization
pygame.init()
display_info = pygame.display.Info()
current_width, current_height = display_info.current_w, display_info.current_h
#screen = pygame.display.set_mode((current_width, current_height), pygame.FULLSCREEN)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setup player
p1 = Player()

running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == KEYDOWN:
         if event.key == K_ESCAPE:
            running = False
   
   screen.fill((0, 0, 0))
   #vert grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pygame.draw.line(screen, (255, 255, 255), (current_width * (_/GRID_DEPTH), 0), (current_width * (_/GRID_DEPTH), current_height))
   #horiz grid
   #for _ in range(1, GRID_DEPTH, 1):
   #   pygame.draw.line(screen, (255, 255, 255), (0, current_height * (_/GRID_DEPTH)), (current_width, current_height * (_/GRID_DEPTH)))

   screen.blit(p1.surface, p1.center_coord)

   pygame.display.update()

pygame.quit()
