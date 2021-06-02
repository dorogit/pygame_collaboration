import pygame

#setting up the screen etc.
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('HangMan')

pygame.draw.rect(screen, (200,200,200),pygame.Rect(300,350,350,200))
pygame.display.update()

run= True

while run:
  pressed= pygame.key.get_pressed()
  if pressed[pygame.K_ESCAPE]:
    break
  pygame.display.update()

