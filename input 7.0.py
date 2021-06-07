answerlist = []

answer = input("Enter any word: ")

if len(answer) > 1 and answer.isalpha():
    answerlist.append(answer)

display = []

used = []

display.extend(answer)

used.extend(display)

for i in range(len(display)):
    display[i] = "_"

print(' '.join(display))
print()

count = 0

incorrect = 5

while count < len(answer) and incorrect > 0:
    guess = input("Enter any letter: ")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1

            used.remove(guess)

    if guess not in display:
        incorrect = incorrect - 1
        print("Wrong guess, You have ", incorrect, "chaces left")

    print("You have guessed : ", count, "correct letters.")
    print("You have" , incorrect, "chances left")

    print(' '.join(display))
    print()

if count ==len(answer):
    print("Well done, you guessed the word")
else:
    print("Unfortunately, you ran out of guesses")
    
