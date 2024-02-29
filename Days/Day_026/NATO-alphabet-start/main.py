import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
'''
#MY FORMAT
#todo 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_026/NATO-alphabet-start/nato_phonetic_alphabet.csv")
all_letters = data['letter'].to_list()
all_codes = data['code'].to_list()

nato_dict = dict(zip(all_letters, all_codes))
#print(nato_dict)

#todo 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Write a word to decode its phonetic:\n").upper()
encoded_word = [nato_dict[letter] for letter in word if letter in nato_dict]

print(encoded_word)
'''
# TEACHER FORMAT

# todo 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv(
    "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_026/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# todo 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(phonetic_dict)

# todo 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word:\n").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
