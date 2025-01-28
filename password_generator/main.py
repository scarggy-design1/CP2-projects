#This is Nicoles password generator

import string
import random

def randomizer(): #Randomizes a giant list containing all characters and prints the amount the user chooses.
    basics = str(string.ascii_letters)
    basics2 = str(string.digits)
    basics3 = str(string.punctuation)
    password = list(basics)
    password2 = list(basics2)
    password3 = list(basics3)
    big_list = password+password2+password3


    required = input("What characters, letters, symbols, or numbers would you like in your code?: ")
    required_list = list(required)
    a = len(required_list)
    
    try: #asks the user for an input of an integer
       num = int(input("How long do you want your password to be?(HAS to be greater than 8) "))
    except ValueError: #if the input is not an integer, it asks again.
        print("Choose a valid NUMBER.")
        return 'error'
    if num < 8: #Makes sure you choose a password that is at LEAST 8 characters long.
        print("Dude, seriously choose a number higher than 8")
        return 'error'

    for i in range(1,5):
        random.shuffle(big_list)
        new_list = big_list[1:num+1-a] #shortens the list so the users required input can be printed in all versions!
        final = new_list+required_list #Adds the users chosen characters to the new list
        random.shuffle(final)
        print(*final, sep='') #gets rid of the[","] and combines the characters together
        print('')

    return 'break'
    
        
        




def main(): #handles the return values.
    while True:
        print("Welcome to random password generator!")
        the_random = randomizer()
        if the_random == 'error':
            randomizer()
        elif the_random == 'break':
            break
        else:
            pass



main() #runs the code