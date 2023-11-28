print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("")

first = str(input(
    'You begin your journey walking along a dirt road until you reach a fork. Would you like to go Left or Right?\n')).strip().upper()[0]

if first == 'L':
    second = str(input("You walk a bit along the dirt road and soon arrive at the riverbank. A bell is hanging on a pole. Would you like to ring the bell and wait, or jump into the river and swim across? (Type 'Ring' or 'Jump')")).strip().upper()[0]
else:
    print('''


                           _______________
                          (               )
                         (                 )              
                        (                   )            
                        |   XXXX     XXXX   |
                        |   XXXX     XXXX   |
                        |   XXX       XXX   |
                        |         X         |
                        \__      XXX     __/
                          |\     XXX     /|
                          | |           | |
                          | I I I I I I I |
                          |  I I I I I I  |
                           \_           _/
                            \_         _/
                              \_______/
                    XXX                        XXX
                  XXXXX                        XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                           XXXXX     XXXXX
                               XXXXXXX
                           XXXXX     XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                  XXXXX                        XXXXX
                    XXX                        XXX
                    
"Oh no! Too late. As you realize, you've walked into quicksand. Slowly, you sink, and unfortunately, you perish!"
          ''')
    print("******GAME OVER!!******")

if second == "R":
    print("A ferryman comes to pick you up.")
    
else:
    print('''
         ,---,                  
  _    _,-'    `--,
 ( `-,'            `)_
  \           ,    o  )
  /   ,       ;        )
 (_,-' \       `, _  ""/
        `-,___ =='__,-'
              ````
                     ,---,
             _    _,-'    `--,
            ( `-,'            `)_
             \           ,    o  )
           le  /   ,       ;        )
            (_,-' \       `, _  ""/
                    `-,___ =='__,-'
                        ````

                           _______________
                          (               )
                         (                 )              
                        (                   )            
                        |   XXXX     XXXX   |
                        |   XXXX     XXXX   |
                        |   XXX       XXX   |
                        |         X         |
                        \__      XXX     __/
                          |\     XXX     /|
                          | |           | |
                          | I I I I I I I |
                          |  I I I I I I  |
                           \_           _/
                            \_         _/
                              \_______/
                    XXX                        XXX
                  XXXXX                        XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                           XXXXX     XXXXX
                               XXXXXXX
                           XXXXX     XXXXX
                   XXXXXXXXXX             XXXXXXXXXX
                  XXXXX                        XXXXX
                    XXX                        XXX
                    
"You hastily decide to swim, but the river is infested with piranhas."
          ''')
    print("******GAME OVER!!******")