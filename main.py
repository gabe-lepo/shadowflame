import pygame
from pygame.locals import *

from globals import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

running = True
circle_x = (1/2) * WIDTH
circle_y = (1/2) * HEIGHT
circle_radius = MAX_SIZE / 2
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      elif event.type == KEYDOWN:
         if event.key == K_ESCAPE:
            running = False
         elif event.key == K_UP:
            circle_y -= circle_radius * 2
         elif event.key == K_DOWN:
            circle_y += circle_radius * 2
         elif event.key == K_RIGHT:
            circle_x += circle_radius * 2
         elif event.key == K_LEFT:
            circle_x -= circle_radius * 2
         elif event.key == K_MINUS:
            circle_radius -= MAX_SIZE / 10
            if circle_radius < MIN_SIZE:
               circle_radius = MAX_SIZE
         elif event.key == K_EQUALS:
            circle_radius += MAX_SIZE / 10
            if circle_radius > MAX_SIZE:
               circle_radius = MIN_SIZE
   
   screen.fill((0, 0, 0))
   #vert grid
   for _ in range(1, GRID_DEPTH, 1):
      pygame.draw.line(screen, (255, 255, 255), (WIDTH * (_/GRID_DEPTH), 0), (WIDTH * (_/GRID_DEPTH), HEIGHT))
   #horiz grid
   for _ in range(1, GRID_DEPTH, 1):
      pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT * (_/GRID_DEPTH)), (WIDTH, HEIGHT * (_/GRID_DEPTH)))

   pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), circle_radius)
   pygame.display.update()

pygame.quit()
