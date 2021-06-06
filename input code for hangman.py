def hangman(word):
    hidden_word = "-" * len(word)
    print("This is the hidden word " + hidden_word)
    while True:
        user_input = input("Guess a letter: ")
        if user_input.isalpha():
            if user_input in word:
                index = word.find(user_input)
                hidden_word = hidden_word[:index] + user_input + hidden_word[index + 1:]
                print(hidden_word)
            else:
                print("Sorry that letter was not found, please try again.")
        else:
            print("Please use letters in the alphabet.")
x = input("Enter your word: ")
hangman(x)