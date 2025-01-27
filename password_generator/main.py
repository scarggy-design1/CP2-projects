#This is Nicoles password generator

import string
import random

def randomizer():
    basics = str(string.ascii_letters)
    basics2 = str(string.digits)
    basics3 = str(string.punctuation)
    password = list(basics)
    
    print(password)

    num = int(input("How long do you want your password to be?(HAS to be greater than 8) "))
    try:
        print(num)
    except ValueError:
        print("Choose a valid NUMBER.")
        return 'error'
    if num < 8:
        print("Dude, seriously choose a number higher than 8")
        return 'error'
    for i in range(1,5):
        random.shuffle(password)
        print(password[1:num])




def main():
    print("Welcome to random password generator!")
    the_random = randomizer()
    if the_random == 'error':
        randomizer()
    else:
        pass



main()