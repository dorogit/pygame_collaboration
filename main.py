import pygame
import time

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
small_text = font4.render('press spacebar',True,(0,0,0))
screen.blit(small_text, (630,222))
screen.blit(input_box_text,((500, 190)))
font = pygame.font.Font(None,32)
input_text = ''
guess = ''
hidden_word = ''
Color = (0,0,0)
Tries = 10
index = 0
letter_in_guessbox = False
convert = False
Fails = 0
draw_once = False

#Game over text
over_font = pygame.font.Font ('freesansbold.ttf', 64)

#Game won text
won_font = pygame.font.Font ('freesansbold.ttf', 64)

#functions for showing 'YOU WIN' and 'GAME OVER' text upon victory or defeat
def game_won():
    won_text = won_font.render ("YOU WIN", True, ( 0, 0, 0))
    screen.blit (won_text, (350, 350))

def game_over_text():
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(450,500,550,500))
    over_text = over_font.render ("GAME OVER", True, (0,0,0))
    screen.blit (over_text, (500, 500))  
 

def guessing(word):
  global hidden_word,index,convert

  for letter in range(len(word)):
    if convert == False:
      hidden_word += '_'
  convert = True
  for chance in range(Tries):
    hidden_word = list(hidden_word)
    word = list(word)
    for alph in word:
      index = index + 1
      if alph == guess:
        hidden_word[index-1] = word[index-1]
    index = 0
    hidden_word = ''.join(hidden_word)
    word = ''.join(word)

#functions for hangman parts and drawing hangman
def draw_head():
  pygame.draw.circle(screen, (0,0,0,), (273,165), 50, width = 9)

def draw_torso():
  pygame.draw.line(screen,(0,0,0), (273, 213), (273,476), width = 12)

def draw_leg1():
  pygame.draw.line(screen,(0,0,0), (273,476),(160, 645), width = 12)

def draw_leg2():
  pygame.draw.line(screen,(0,0,0), (273,476),(380,645), width = 12)

def draw_arm1():
  pygame.draw.line(screen, (0,0,0), (275, 300),(180,180),width = 12)

def draw_arm2():
  pygame.draw.line(screen, (0,0,0),(275, 300),(360,180),width = 12)

def Hang():
  pygame.draw.rect(screen, (200,200,200), pygame.Rect(150,110,275,560))
  pygame.draw.line(screen, (0,0,0), (273,50),(273,200),width = 9)
  pygame.draw.circle(screen, (0,0,0,), (300,240), 50, width = 9)
  pygame.draw.line(screen,(0,0,0), (273, 278), (273,551), width = 12)
  pygame.draw.line(screen,(0,0,0), (273,551),(160, 720), width = 12)
  pygame.draw.line(screen,(0,0,0), (273,551),(380,720), width = 12)
  pygame.draw.line(screen, (0,0,0), (275, 375),(180,255),width = 12)
  pygame.draw.line(screen, (0,0,0),(275, 375),(360,255),width = 12)


run = True
typing = True
typing2 = False
while run:
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_ESCAPE]:
    break
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    if event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:

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
        if event.key == pygame.K_SPACE:

          #rendering text for letter input box and removing the old text
          typing = False
          typing2 = True
          pygame.draw.rect(screen, (0,0,0), input_box)
          pygame.draw.rect(screen, (200,200,200),pygame.Rect(499,190,500,33))
          pygame.draw.rect(screen, (200,200,200),pygame.Rect(630,222,300,20))
          guess_text = font3.render('Guess a letter from the word',True, (0,0,0))
          small_text2 = font4.render('(press enter)',True,(0,0,0))
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


        if event.key == pygame.K_RETURN and typing2 == True:
          guessing(word)

          #putting a rect to hide old text
          pygame.draw.rect(screen, (200,200,200), pygame.Rect(500,500,500,500))

          #calling the guess function upon entering
          guessing(word)

          #blitting the hidden word and other text
          hidden_word_text = font1.render(hidden_word,True, (0,0,0))
          screen.blit(hidden_word_text, (500,500)) 
          if guess not in word:
            Tries = Tries - 1
            Fails += 1
          if Tries <=0:
            time.sleep(3)
            run = False
          Tries_string = 'Tries remaining : {}'.format(Tries)
          Tries_text = font1.render(Tries_string,True,(0,0,0))
          screen.blit(Tries_text, (450,600))

          #if player completely guesses the word
          if hidden_word == word and Tries >=0:
            font0 = pygame.font.Font(None,50)
            pygame.draw.rect(screen, (200,200,200), pygame.Rect(400,500,500,500))
            hangman_text = font0.render('HangMan Lives ', True,(0,0,0))
            screen.blit(hangman_text,(500,500))
            game_won()
          
          #drawing hangman upon failure of guesses
          if Fails == 2 and guess not in word and draw_once == False:
            draw_head()
            draw_once = True

          if Fails == 3 and guess not in word and draw_once == False:
            draw_torso()
            draw_once = True

          if Fails == 4 and guess not in word and draw_once == False:
            draw_leg1()
            draw_once = True
          
          if Fails == 5 and guess not in word and draw_once == False:
            draw_leg2()
            draw_once = True
           
          if Fails == 6 and guess not in word and draw_once == False:
            draw_arm1()
            draw_once = True
          
          if Fails == 7 and guess not in word and draw_once == False:
            draw_arm2()
            draw_once = True
          
          if Fails == 8 and guess not in word and draw_once == False:
            Hang()
            game_over_text()

          #draw one variable is used such that on pressing enter a single body 
          #part will be shown on 1 failure insted of all at once
          draw_once = False

        #blitting text box and rendering text the input
        pygame.draw.rect(screen, Color, input_box)
        text = font.render(guess, True , (200,200,200))
        screen.blit(text,(input_box.x+5, input_box.y+5))

        #to ensure text doesnt move out of the box
        input_box.w = max(100,text.get_width()+10)
        pygame.display.update()


  pygame.display.update()
  Clock.tick(60)
print(pygame.mouse.get_pos())
