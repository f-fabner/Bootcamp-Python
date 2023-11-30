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

first = str(input('You begin your journey walking along a dirt road until you reach a fork. Would you like to go Left or Right?\n')).strip().upper()[0]

if first == 'L':
  second = str(input("You walk a bit along the dirt road and soon arrive at the riverbank. A bell is hanging on a pole. Would you like to ring the bell and wait, or jump into the river and swim across? (Type 'Ring' or 'Jump')")).strip().upper()[0]
  if second == "R":
    print('''
You walk to the post, ring the bell, and wait for a while. A boatman approaches, docks the boat, you board, and then he ferries you across the river to the other side.
              _______________
  ~~~~~~~~~~~~\             /~~~~~~~~~~
      ~~    ~~~\___________/~~~~~~   ~~
  ~~~~~~     ~  ~~~   ~ ~~~~     ~~~~~~ 
          ''')
    third = str(input('''After crossing the river, continue your journey. The dirt road transforms into a rocky path that leads to a small cave. This cave seems to have been designed as some kind of dungeon...

***************************************************
*                 /   \              /'\       _  *
*.           /'.,/     \_         .,'   \     / \_*
* \         /            \      _/       \_  /    *
*  \__,.   /              \    /           \/.,   *
*       \_/                \  /',.,''\      \_ \_/*
*                        _  \/   /    ',../',.\   *
*          /           _/m\  \  /    |         \  *
*        _/           /MMmm\  \_     |          \/*
*       /      \     |MMMMmm|   \__   \          \*
*               \   /MMMMMMm|      \   \          *
*                \  |MMMMMMmm\      \___          *
*                 \|MMMMMMMMmm|____.'  /\_        *
 **************************************************

Upon entering the dungeon, you encounter three doors, each with a plaque of a different color. Which door would you like to enter? The red one, the blue one, the yellow one, or would you prefer to backtrack? (Chose: Red, Blue, Yellow, Go Back)\n''')).strip().upper()[0]

    if third == "R":
      print('''
        ,.   (   .      )        .      "
      ("     )  )'     ,'        )  . (`     '`
    .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
    _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '
                    ,.   (   .      )        .      "
                  ("     )  )'     ,'        )  . (`     '`
                .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '
        ,.   (   .      )        .      "
      ("     )  )'     ,'        )  . (`     '`
    .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
    _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '
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
                        
    ""Upon entering the red room, the door closes behind you, and the room is engulfed in flames, leading to your demise.""
              ''')
      
      print("******GAME OVER!!******")
      
    elif third == "B":
      print('''
                      (    )
                      ((((()))
                      |o\ /o)|
                      ( (  _')
                      (._.  /\__
                      ,\___,/ '  ')
        '.,_,,       (  .- .   .    )
        \   \_\     ( '        )(    )
          \   \_\    \.  _.__ ____( .  |
          \  /\.\   .(   .'  /\  '.  )
            \(  \.\.-' ( /    \/    \)
            '  ()) _'.-|/\/\/\/\/\|
                '\.\ .( |\/\/\/\/\/|
                  '((  \    /\    /
                  ((((  '.__\/__.')
                    ((,) /   ((()   )
                    "..-,  (()("   /
                pils  _//.   ((() ."
              _____ //,/" ___ ((( ', ___
                              ((  )
                                / /
                              _/,/'
                            /,/,"
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
                        

    Upon entering the blue room, you hear a diabolical hiss. A beast with an axe was waiting for you. It strikes you with its large axe, and you fall unconscious, succumbing to death.
    ''')
      
      print("******GAME OVER!!******")
    
    elif third == "Y":
      print('''You enter the room and see an illuminated pedestal. On top of it lies an amulet with a note that reads, 'Noble warrior who has made it this far, this is the Amulet of Life. Make good use of its power!' 
          
                   o--o--=g=--o--o     
                 ./      .'       \.
                 o      '.         o
                  \               /
                   o            o
                    \          /
                     o        o
                      \      /
                       o    o
                        \../
                         ||                     
                       _.^^.__
                      ( ,-.-. )
                      | `. ,' |
                      (   `   )
                       ```````
            
            
            ''')
      
      print("***Congratulations, you are the great WINNER!!***")
      
    else:
      print('''
                  \|/
                .-*-         
              / /|\         
              _L_            
            ,"   ".          
          /       \      
          |         |      
          \       /         
          _/.___,\_      
          
                        \|/
                        .-*-         
                      / /|\         
                      _L_            
                    ,"   ".          
                  /       \      
                  |         |      
                  \       /         
                  _/.___,\_      
                
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
                        

    While attempting to backtrack, you inadvertently step into a trap. You hear a click, and suddenly, a trapdoor in the ceiling opens, dropping two bombs on you. They explode, leaving nothing behind to tell the tale.
    ''')
      
      print("******GAME OVER!!******")
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
            ( `-,'            ` )_
             \           ,    o   )
             /   ,       ;         )
            (_,-' \       `, _   ""/
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