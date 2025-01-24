#This is Nicoles password generator

import string


def randomizer():
    print("Welcome to random password generator! This program will print 4 passwords that meet your criteria. ")
    criteria = input("""What is your criteria?:
                     REQUIRED: has to have at least 1 special charcater and 1 number.
                     1. include specifics special characters (you choose)
                     2. Include specific numbers (you choose)
                     3. Include specific words/phrases (you choose)
                     4. exit
                     \n""")
    if criteria == '1':
        a2 = string.punctuation
        a = input(f"You can pick any specical characters! They include: {a2}\n")
        required_specials = []
        required_specials.append(a)
        print("You chose:\n", required_specials)
    
    elif criteria == '2':
        b2 = string.digits
        b = input(f"You can pick any digits! They include: {b2}\n")
        required_digits = []
        required_digits.append(b)
        print("You chose:\n", required_digits)
    elif criteria == '3':
        c2 = string.digits
        c = input(f"You can pick any words/phrases! They include: {c2}\n")
        required_phrase = []
        required_phrase.append(c)
        print("You chose:\n", required_phrase)
    elif criteria == '4':
        return 'exit'
    else:
        print("not a valid choice. Pick again\n")

randomizer()


"LaRose, Miller, K"

"Blunt, Shurtz, Childress, Lamb,"