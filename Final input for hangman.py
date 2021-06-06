word = input("Enter any word: ")

print("Guess the characters")
 
guesses = ''
 
chances = 6
 
while chances > 0:
     
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
             
        else:
            print("_")
            failed += 1
             
 
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
         
        chances -= 1
        print("Wrong")
        print("You have", + chances, 'more guesses')
         
         
        if chances == 0:
            print("You Loose")
