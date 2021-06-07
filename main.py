import pygame
from pygame.constants import K_RETURN

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
small_text = font4.render('press enter',True,(0,0,0))
screen.blit(small_text, (630,222))
screen.blit(input_box_text,((500, 190)))
font = pygame.font.Font(None,32)
input_text = ''
guess = ''
hidden_word = ''
Color = (0,0,0)
Tries = 5
num = 0
letter_in_guessbox = False


#functions for hangman parts
def draw_head():
  pygame.draw.circle(screen, (0,0,0,), (273,165), 50, width = 7)

def draw_torso():
  pygame.draw.line(screen,(0,0,0), (273, 213), (273,476), width = 7)

def draw_leg1():
  pygame.draw.line(screen,(0,0,0), (273,476),(163, 645), width = 7)

def draw_leg2():
  pygame.draw.line(screen,(0,0,0), (273,476),(373,645), width = 7)
#incomplete 


run = True
typing = True
typing2 = False
run = True
typing = True
typing2 = False
while run:

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_ESCAPE]:
    break
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

      if typing == True:
        
        if event.key == pygame.K_BACKSPACE:
          
          input_text = input_text[:-1]

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
        if event.key == pygame.K_RETURN:

          #rendering text for letter input box and removing the old text
          typing = False
          typing2 = True
          pygame.draw.rect(screen, (0,0,0), input_box)
          pygame.draw.rect(screen, (200,200,200),pygame.Rect(499,190,500,33))
          pygame.draw.rect(screen, (200,200,200),pygame.Rect(630,222,300,20))
          guess_text = font3.render('Letter to be guessed goes here',True, (0,0,0))
          small_text2 = font4.render('1 at a time',True,(0,0,0))
          screen.blit(small_text2,((630,222)))
          screen.blit(guess_text,((500, 190)))
      
      word = input_text

      if typing2 == True:
        
        if event.key == pygame.K_BACKSPACE and letter_in_guessbox == True:
          #to ensure only 1 letter is allowed in the guessbox
          guess = guess[:-1]   
          letter_in_guessbox = False       
        #converting keys to text
        elif event.key!=pygame.K_RETURN and event.key!=pygame.K_ESCAPE:
          #checking if input is alphabet
          if letter_in_guessbox == False:
            if event.unicode.isalpha():
              guess = event.unicode
              letter_in_guessbox = True

        for letter in range(len(word)):
          hidden_word += '_'
        for chance in range(Tries):
          hidden_word = list(hidden_word)
          word = list(word)
          for alph in word:
            if alph == guess: 
              hidden_word[num] = word[num]
            num = num + 1
          num = 0
          hidden_word = ''.join(hidden_word)
          word = ''.join(word)
        if event.key == pygame.K_RETURN and typing2 == True:
          Tries = Tries - 1
          print(hidden_word)
        #blitting text box and rendering text
        pygame.draw.rect(screen, Color, input_box)
        text = font.render(guess, True , (200,200,200))
        screen.blit(text,(input_box.x+5, input_box.y+5))

        #to ensure text doesnt move out of the box
        input_box.w = max(100,text.get_width()+10)
        pygame.display.update()

  pygame.display.update()
  Clock.tick(60)
print(pygame.mouse.get_pos())
