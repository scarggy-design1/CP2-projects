
from character_creation import create as creation

def main():
    while True:
        ask = input("WELCOME TO\n-- THE GAME --\nBefore you play, what would you like to do?\n1) CREATE character\n2) Pick precreated character\n3) EXIT").strip()
        if ask == '1':
            creation()
        elif ask == '2':
            pass
        elif ask == '3':
            break
        
