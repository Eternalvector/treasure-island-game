print(r'''
    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Direction = input("Do you go Left or Right?").upper()

if Direction=="LEFT" or Direction=="L":
    print("You proceed ahead and see a river.")
    Swim = input("Do you swim or wait?").upper()
    if Swim=="WAIT":
        print("Three doors appear in front of you.")
        Door = input("Which door do you select: Red, Yellow or Blue?").upper()
        if Door == "RED" or Door == "R":
            print("You were burned by fire. GAME OVER!")
        elif Door == "BLUE" or Door == "B":
            print("You were eaten by beasts. GAME OVER!")
        elif Door == "YELLOW" or Door == "Y":
            print("You found the treasure! GOOD JOB!")
            print('''                                 _       
                                            | |      
              ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
             / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
            | (_| (_) | | | | (_| | | | (_| | |_\__ \
             \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                              __/ |                  
                             |___/   ''')
        else:
            print("There is no such option and the sky collapsed on you. GAME OVER!")
    else:
        print("You were attacked by a Trout. GAME OVER!")

else:
    print("You fell into a hole. GAME OVER!")












