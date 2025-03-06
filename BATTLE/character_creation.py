import random

def create():
    name = input("Welcome to CREATION...\nWhat do you want to name your character?: ")
    try:
        points = 20
        speed = int(input("What is the speed of your character? "))
        points-speed
        health = int(input("What is the health of your character? "))
        points-health
        brawn = int(input("What is the strength of your character? "))
        points-brawn
        defense = int(input("What is the defense of your character? "))
        points-defense
        if points != 0:
            continue
        else:
            pass
    except:
        print('DUDE.\nOkay freak actually pick a number thats valid.\n')
        continue