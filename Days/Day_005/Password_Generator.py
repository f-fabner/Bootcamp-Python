import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('**********************')
print('* PASSWORD GENERATOR *')
print('**********************')
#perguntas sobre as características do password
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#lista vazia inicial do password
password_list = []
#loop pra adicionar a quantidade de letras pedidas na primeira pergunta
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
#loop pra adicionar a quantidade de siímbolos pedidos na segunda pergunta
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
#loop pra adicionar a quantidade de números pedidos na terceira pergunta
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
#randon e shuffle pra embaralhar a lista de forma aleatórioa
random.shuffle(password_list)
#o password final recebe uma string fazia inicial
password = ""
#loop pra receber cada caractere da lista anterior dentro da string vazia
for char in password_list:
  password += char
#imprime na tela a string preenchida finalmente
print('------------------------')
print(f"Your password is:\n{password}")
print('------------------------')
