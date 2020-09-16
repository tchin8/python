import random

random = random.randint(0, 20)
guesses = 10

name = input("Hello! What is your name? ")
print(name)
print(f'Well, {name}, I am thinking of a number between 0 and 20')

gameOver = False
while not gameOver:
  response = int(input("Take a guess. "))
  print(response)
  if response > random:
    print('Your guess is too high.')
    guesses -= 1
  elif response < random:
    print('Your guess is too low.')
    guesses -= 1
  
  if guesses == 0 or response == random:
    gameOver = True

if guesses == 0:
  print(f'Sorry, {name}. You could not guess my number {random}.')
else:
  print(f'Good job {name}! You guessed the number in {10-guesses} guesses!')
