import pygame
pygame.init()

#setting up the screen etc.
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('HangMan')

gallow = pygame.image.load('gallow.png')
screen.fill((200,200,200))
Clock = pygame.time.Clock()
pygame.display.update()

run= True

while run:
  event = pygame.event.wait()
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_ESCAPE]:
    break
  pygame.display.update()
  Clock.tick(30)
  screen.blit(gallow,((0,0)))
