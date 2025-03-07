
from character_creation import create as creation, characters as character

def main():
    while True:
        ask = input("WELCOME TO (drum roll please)\n-- THE GAME --\nBefore you play, what would you like to do?\n1) CREATE character\n2) PICK precreated character\n3) EXIT").strip()
        if ask == '1':
            creation()
        elif ask == '2':
            character()
        elif ask == '3':
            break
        else:
            print("INVALID\nChoose a VALID answer dood.")
        

main()