# pygame_collaboration

Repository for making a PyGame “HangMan” 
A collab by Ameya and Ishaan

HangMan is a word-guessing two-player game in which one player creates a word to be guessed
then, all the letters of the word will be shown represented as dashes(-) and the guesser 
must pick an alphabet. If the alphabet is a part of the word, all letters of guessed alphabet 
will appear instead of the dashes. Using this concept, to achieve victory,
the guesser must guess the entire word or,guess all letters of the word, so to say. 
Now the part which makes the game "HangMan" is that there will also be a Gallow 
while the other player is guessing a word. Each time the other player guesses a wrong alphabet,
a part of a stickman will be drawn on the gallow. If the player fails to guess the word before the 
stickman is completed, the stickman will be complete and hanged, hence marking defeat of the guesser.

This is the concept behind HangMan.


what to implement in order to make HangMan fucntional:
-An input window to take input of the word which is to be guessed and the alphabet guessed by the other player
-A *RULES* button to take the user to a window which will display rules and info of the game
-A function to convert the word given by the player to dashes, and make letters appear when corrosponding alphabet is guessed
-A function to draw lines of the stickman/ draw the stickman's limbs each time a wrong alphabet is guessed
-A *Hanging animation* upon the guesser's defeat for the quality of the game
-Already blitted-and-updated Gallow made up of lines and rectangles along with the stickman's head(circle) as a starting point
-"Play again" and "Quit" buttons (optional once the game's main algorithm is complete)
