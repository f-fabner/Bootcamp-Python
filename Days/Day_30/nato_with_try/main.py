import pandas

data = pandas.read_csv(
    "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/nato_with_try/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#My Method
while True:
    try:
        word = input("enter a word:\n").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        break

    except:
        print("Sorry, only letters in the alphabet please.")
        
'''
# Teacher Method
def generate_phonetic():
    word = input("enter a word:\n").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
'''