import random
import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_answer(guess, secret, guesses):
  clear()
  print(logo)
  if guess > secret:
    print("~↑~↑~↑~Too high.~↑~↑~↑~")
    return guesses - 1
  elif guess < secret:
    print("~↓~↓~↓~Too low.~↓~↓~↓~")
    return guesses - 1
  else:
    print(f"****You got it!****\nThe answer was {secret}!!!!")
    
secret = random.randint(0,100)
guesses = 0

print(logo)
while True:
    Difficulty = input(str("Welcome to the Number Guessing Game!\nI'm Thinking of a number between 1 an 100.\nChoose a difficulty! Type 'easy' or 'hard':\n")).strip().upper()[0]
    if Difficulty in "EH":
        if Difficulty == "E":
            guesses = 10            
            break
        elif Difficulty == "H":
            guesses = 5
            break
    while True:
       
        Difficulty = input(str("ERROR! Type 'easy' or 'hard:\n")).strip().upper()[0]
        
        if Difficulty in "EH":
            break
        print("ERROR! Please, type 'easy' or 'hard'.")
    
    if Difficulty == "E":
        guesses = 10            
        break
    elif Difficulty == "H":
        guesses = 5
        break

guess = 0
while guess != secret:    
    print(f"You have {guesses} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    guesses = check_answer(guess, secret, guesses)
    if guesses == 0:
        print("You've run out of guesses, you lose.")
        break
    elif guess != secret:
        print("Guess again.")