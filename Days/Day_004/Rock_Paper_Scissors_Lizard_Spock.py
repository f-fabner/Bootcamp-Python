import random
import time
print()
print('======== DESAFIO 45 ========')
print()
print('**********************')
print('* JO!!! KEN!!! PO!!! *')
print('**********************')
print()
NUM = random.randint(1, 5)
T = int(input('''Escolha entre:
[ 1 ] - ✊ - Pedra
[ 2 ] - 🖐️ - Papel
[ 3 ] - ✌️ - Tesoura
[ 4 ] - 🤏 - Lagarto
[ 5 ] - 🖖 - Spock\n'''))
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
    print('\033[33mEMPATOU!\033[m')
    if NUM == 1:
        print('💻 ✊ x ✊ 🙍')
    elif NUM == 2:
        print('💻 🖐️ x 🖐️ 🙍')
    elif NUM == 3:
        print('💻 ✌️ x ✌️ 🙍')
    elif NUM == 4:
        print('💻 🤏 x 🤏 🙍')
    elif NUM == 5:
        print('💻 🖖 x 🖖 🙍')
#COMPUTADOR JOGANDO PEDRA
elif NUM == 1 and T == 2:
    print('VOCÊ \033[32mVENCEU!\033[m')
    print('💻 ✊ x 🖐️🙍 ')
elif NUM == 1 and T == 3:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 ✊ x ✌️ 🙍')
elif NUM == 1 and T == 4:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 ✊ x 🤏 🙍')
elif NUM == 1 and T == 5:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 ✊ x 🖖 🙍')
#COMPUTADOR JOGANDO PAPEL
elif NUM == 2 and T == 1:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🖐️ x ✊ 🙍')
elif NUM == 2 and T == 3:
    print('VOCÊ \033[32mVENCEU!\033[m')
    print('💻 🖐️ x ✌️ 🙍')
elif NUM == 2 and T == 4:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🖐️ x 🤏 🙍')
elif NUM == 2 and T == 5:
    print('VOCE \033[32mVENCEU!\033[m')
    print('💻 🖐️ x 🖖 🙍')
#COMPUTADOR JOGANDO TESOURA
elif NUM == 3 and T == 1:
    print('VOCÊ \033[32mVENCEU!\033[m')
    print('💻 ✌️ x ✊ 🙍')
elif NUM == 3 and T == 2:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 ✌️ x 🖐️ 🙍')
elif NUM == 3 and T == 4:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 ✌️ x 🤏 🙍')
elif NUM == 3 and T == 5:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 ✌️ x 🖖 🙍')
#COMPUTADOR JOGANDO LAGARTO
elif NUM == 4 and T == 1:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 🤏 x ✊ 🙍')
elif NUM == 4 and T == 2:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🤏 x 🖐️ 🙍')
elif NUM == 4 and T == 3:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 🤏 x ✌️ 🙍')
elif NUM == 4 and T == 5:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🤏 x 🖖 🙍')
#COMPUTADOR JOGANDO SPOCK  
elif NUM == 5 and T == 1:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 🖖 x ✊ 🙍')
elif NUM == 5 and T == 2:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🖖 x 🖐️ 🙍')
elif NUM == 5 and T == 3:
    print('VOCE \033[32mGANHOU!\033[m')
    print('💻 🖖 x ✌️ 🙍')
elif NUM == 5 and T == 4:
    print('VOCE \033[31mPERDEU!\033[m')
    print('💻 🖖 x 🤏 🙍')  
else:
    print('\033[41mINVALIDO!\033[mPARA DE COLCOAR OUTROS SIMBOLOS!')