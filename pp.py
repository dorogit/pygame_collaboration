string = input(str("enter"))

guess = ''
hidden_word = ''
Chances = 5
num = 0
for letter in range(len(string)):
  hidden_word += '_'
for chance in range(Chances):
  guess = input(str('guess '))
  hidden_word = list(hidden_word)
  string = list(string)
  for alph in string:
    if alph == guess: 
      hidden_word[num] = string[num]
    num = num + 1
  num = 0
  hidden_word = ''.join(hidden_word)
  string = ''.join(string)
  print(hidden_word)

  if guess not in string:
    print('wrong guess')
print('Lost lol')