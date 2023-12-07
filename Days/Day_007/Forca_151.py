import os
import random
from hangman_pokemons import pokemon_151
from hangman_art import stages, logo, prize, miau

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
chosen_pokemon = random.choice(pokemon_151).lower()

lives = 6
print(logo)
display = []
pokemon_length = len(chosen_pokemon)

for _ in range(pokemon_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    clear()
    
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(pokemon_length):
        letter = chosen_pokemon[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_pokemon:
        print("You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!!")
            print(miau)
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You WIN!!")
        print(prize)
        
    print(stages[lives])