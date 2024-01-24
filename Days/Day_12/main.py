#WIP

import random
import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
secret = random.randint(0,100)
guesses = 0

print(logo)
while True:
    Difficulty = input(str("Wlecome to the Number Guessing Game!\nI'm Thinking of a number between 1 an 100.\nChoose a difficulty! Type 'easy' or 'hard':\n")).strip().upper()[0]
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



print(secret)
print(Difficulty)
print(guesses)