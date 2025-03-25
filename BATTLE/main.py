import time
from character_creation import create as creation
from main_battle_interface import main_game as main_g

def main(): #main user interface
    while True:
        time.sleep(0.5)#pauses execution for 1/2 second
        ask = input("WELCOME TO (drum roll please)\n-- THE GAME --\nBefore you play, what would you like to do?\n1) CREATE character\n2) PICK precreated character\n3) EXIT\n").strip()
        if ask == '1':
            creation()
            main_g()
        elif ask == '2':
            main_g()
        elif ask == '3':
            break
        else:
            print("INVALID\nChoose a VALID answer dood.")
        

main()


