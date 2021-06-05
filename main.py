import pygame
import sys

pygame.init()

#setting up the screen etc.
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('HangMan')

gallow = pygame.image.load('gallow.png')
screen.fill((200,200,200))
Clock = pygame.time.Clock()
screen.blit(gallow,((-60,20)))

#music
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1)

#HangMan
font1 = pygame.font.Font(None, 70)
img1 = font1.render('HANGMAN',True, (0,0,0))
screen.blit(img1,(375,40))

input_box = pygame.Rect(430,250,550,50)
font = pygame.font.Font(None,32)
input_text = ''
Color = (0,0,0)

run = True
typing = True
while run:
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_ESCAPE]:
    break
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if typing == True:
        
        if event.key == pygame.K_BACKSPACE:
          
          input_text = input_text[:-1]

        else:
          input_text += event.unicode

        pygame.draw.rect(screen, Color, input_box)
        text = font.render(input_text, True , (200,200,200))
        screen.blit(text,(input_box.x+5, input_box.y+5))

        #to ensure text doesnt move out of the box
        input_box.w = max(100,text.get_width()+10)
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
      typing = False
  Clock.tick(60)
