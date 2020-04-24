import random

#This is my first ever project#
#Help Screen#
def help_screen():
    print("""              
    
                      ~Help~
                      
    How to play: Once you have started the program,
    you will choose a dice to roll from the provided
    list, once selected the program will roll said
    dice and give you a randomly generated result.
    
    Press 1 to play the game
    Press 2 to return to menu
    
    **This Program was written by Grant Walker April 2020**
    
    """)

    help_screen_number = input("Please choose a option: ")
    try:
        help_screen_int = int(help_screen_number)
        print("you have selected: ", help_screen_int)
    except ValueError:
        print(" Invalid Selection! ")
        help_screen()

    if help_screen_int == 1:
        gamescreen()
    if help_screen_int == 2:
        menu_screen()
    else:
        print("Invalid Selection! Please try again")
        menu_screen()


# GameScreen#
def gamescreen():
    print("""
    Welcome brave adventurer to the dice roller!
    May the rolls forever be in your favor

    Please select a dice to roll:
    Press 1 for a D4
    Press 2 for a D6
    Press 3 for a D10
    Press 4 for a D12
    Press 5 for a D20
    Press 6 to return to menu

    """)

    gamescreen_number = input("Please select an option: ")
    try:
        gamescreen_int = int(gamescreen_number)
        print("you have selected: ", gamescreen_int)
    except ValueError:
        print(" Invalid Selection! ")
        gamescreen()

    if gamescreen_int == 1:
        selected = random.randint(1,4)
        print("Your dice roll is: ", selected)
        gamescreen()
    if gamescreen_int == 2:
        selected = random.randint(1, 6)
        print("Your dice roll is: ", selected)
        gamescreen()
    if gamescreen_int == 3:
        selected = random.randint(1,10)
        print("Your dice roll is: ", selected)
        gamescreen()
    if gamescreen_int == 4:
        selected = random.randint(1,12)
        print("Your dice roll is: ", selected)
        gamescreen()
    if gamescreen_int == 5:
        selected = random.randint(1,20)
        print("Your dice roll is: ", selected)
        gamescreen()
    if gamescreen_int == 6:
        menu_screen()
    if gamescreen_int == 100:
        selected = random.randint(1,100)
        print("""Haha! You have found the fabled 100D!
        It has rolled:""", selected)
        gamescreen()
    else:
        print("Invalid Selection! Please try again")
        gamescreen()


#Menu Screen#
def menu_screen():
    print(""" 
    
     ~Main Menu~ 
     
    Press 1 to Play
    Press 2 for Help
    Press 3 to Quit
    
    """)

    menu_selection_number = input("Please choose a option: ")
    try:
        menu_selection_int = int(menu_selection_number)
        print("you have selected: ", menu_selection_int)
    except ValueError:
        print(" Invalid Selection! ")
        menu_screen()

    if menu_selection_int == 1:
        gamescreen()
    elif menu_selection_int == 2:
        help_screen()
    elif menu_selection_int == 3:
        exit()
    elif menu_selection_int == 69: #Keeping this for meme reasons
        print("Nice...")
        menu_screen()
    elif menu_selection_int == 42: #Keeping this for meme reasons
        print("The ultimate answer to life, the universe and everything...")
        menu_screen()
    else:
        print("Invalid Selection! Please try again")
        menu_screen()

#Opening#
print("""

#####         ####     #####    ####   #####
#             #   ##     #     ##   #  #
####   ###    #    ##    #    ##       ####
#             #   ##     #     ##   #  #
#####         ####     #####    ####   ##### 
""")

name = input("Please type your name:")

print("Welcome, " +name+ ", what can we do for you today?" )

menu_screen()