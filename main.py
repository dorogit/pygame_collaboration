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

#assigning necessary variables and values, blitting text etc.
input_box = pygame.Rect(430,250,550,50)
font3 = pygame.font.Font(None, 43)
font4 = pygame.font.Font(None, 30)
input_box_text = font3.render('Word to be guessed goes here',True, (0,0,0))
small_text = font4.render('(press enter)',True,(0,0,0))
screen.blit(small_text, (630,222))
screen.blit(input_box_text,((500, 190)))
font = pygame.font.Font(None,32)
input_text = ''
Color = (0,0,0)
Tries = 5

#functions for hangman parts

def draw_head():
  pygame.draw.circle(screen, (0,0,0,), (273,165), 50, width = 7)

def draw_torso():
  pygame.draw.line(screen,(0,0,0), (273, 213), (273,476), width = 7)

def draw_leg1():
  pygame.draw.line(screen,(0,0,0), (273,476),(163, 645), width = 7)

def draw_leg2():
  pygame.draw.line(screen,(0,0,0), (273,476),(373,645), width = 7)



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

        #this part is for terminating input and starting the hangman blitting
        if event.key == pygame.K_RETURN:
          if typing != False:
            typing = False
            
          if Tries == 5:
            draw_head()
            Tries -=1
            
          if Tries == 4:
            draw_torso()
            Tries -=1
            
          if Tries == 3:
            draw_leg1()
            Tries -=1
  
          if Tries == 2:
            draw_leg2()
            Tries -=1
          
        #converting keys to text
        elif event.key!=pygame.K_RETURN and event.key!=pygame.K_ESCAPE:
          #checking if input is alphabet
          if event.unicode.isalpha():
            input_text += event.unicode
        
        #blitting text box and rendering text
        pygame.draw.rect(screen, Color, input_box)
        text = font.render(input_text, True , (200,200,200))
        screen.blit(text,(input_box.x+5, input_box.y+5))

        #to ensure text doesnt move out of the box
        input_box.w = max(100,text.get_width()+10)
        pygame.display.update()
  pygame.display.update()
  Clock.tick(60)
print(pygame.mouse.get_pos())
