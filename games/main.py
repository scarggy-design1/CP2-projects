#This is Nicole's simple game user interface
from games import one_ten as ten, one_hundred as hundred


def simple_game_main():
    oneTen = ten()
    oneHundred = hundred()
    while True:
        choice = input("Welcome to the SIMPLE GUESSING GAME!\n What would you like to do? \n 1) Guess 1-10\n 2) Guess 1-100\n 3) EXIT to the main menu")
        if choice == '1':
            while True:
                if oneTen == 'again':
                    pass
                elif oneTen == 'end':
                    break  
        elif choice == '2':
            while True:
                if oneHundred == 'again':
                    pass
                elif 'end' in oneHundred:
                    break
        elif choice == '3':
            break