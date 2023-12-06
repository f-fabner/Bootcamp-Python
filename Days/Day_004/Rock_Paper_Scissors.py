import random
import time
print()
print('======== DESAFIO 45 ========')
print()
print('**********************')
print('* JO!!! KEN!!! PO!!! *')
print('**********************')
print()
NUM = random.randint(1, 3)
T = int(input('Escolha entre:\n1 - ✊ - Pedra\n2 - 🖐️ - Papel\n3 - ✌️ - Tesoura\n'))
print()
print('👊👊')
time.sleep(1)
print ('JO!!!🤜🤛\n')
time.sleep(1)
print('👊👊')
time.sleep(1)
print('KEN!!!🤜🤛\n')
time.sleep(1)
print('👊👊')
time.sleep(1)
print('PO!!!🤜🤛\n')
time.sleep(1)
if NUM == T:
    print('EMPATOU!')
    if NUM == 1:
        print('💻 ✊ x ✊ 🙍')
    elif NUM == 2:
        print('💻 🖐️ x 🖐️ 🙍')
    elif NUM == 3:
        print('💻 ✌️ x ✌️ 🙍')
elif NUM == 1 and T == 2:
    print('VOCÊ VENCEU!')
    print('💻 ✊ x 🖐️🙍 ')
elif NUM == 1 and T == 3:
    print('VOCE PERDEU!')
    print('💻 ✊ x ✌️ 🙍')
elif NUM == 2 and T == 1:
    print('VOCE PERDEU!')
    print('💻 🖐️ x ✊ 🙍')
elif NUM == 2 and T == 3:
    print('VOCÊ VENCEU!')
    print('💻 🖐️ x ✌️ 🙍')
elif NUM == 3 and T == 1:
    print('VOCÊ VENCEU!')
    print('💻 ✌️ x ✊ 🙍')
elif NUM == 3 and T == 2:
    print('VOCE PERDEU!')
    print('💻 ✌️ x 🖐️ 🙍')
else:
    print('INVALIDO!PARA DE COLOCAR OUTROS SIMBOLOS!')