from art import logo, vs
from game_data import data
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sort_insta():
    if not data:
        return None

    insta = random.randint(0, len(data) - 1)
    what_insta = data.pop(insta)
    return what_insta

def answer(guess, a_followers, b_followers): 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b" 

def game():
    print(logo)
    insta_01 = sort_insta()
    insta_02 = sort_insta()
    score = 0
    loop_game = True

    while loop_game:
        insta_01 = insta_02
        insta_02 = sort_insta()
                
        while insta_01 == insta_02:
            insta_02 = sort_insta()
            
        print(f"Compare A: {insta_01['name']}, a {insta_01['description']}, from {insta_01['country']}.")
        print(vs)
        print(f"Against B: {insta_02['name']}, a {insta_02['description']}, from {insta_02['country']}. ")
        
        response = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        a_follower = insta_01['follower_count']
        b_follower = insta_02['follower_count']
        is_correct = answer(response, a_follower, b_follower)
        
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            loop_game = False
            print(f"Sorry, that's wrong. Final score: {score}")
clear()
game()