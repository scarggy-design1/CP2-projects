import random
import csv

def checker(x):
    if x == 0:
        pass
    elif x > 20:
        return 'negative'
    elif x < 0:
        return 'over'
    else:
        pass

def create():
    name = input("Welcome to CREATION...\nWhat do you want to name your character?: ")
    try:
        points = 20
        speed = int(input(f"What is the speed of your character? You have {points} points left\n"))
        points-=speed
        checker(points)
        health = int(input(f"What is the health of your character? You have {points} points left\n"))
        points-=health
        checker(points)
        brawn = int(input(f"What is the strength of your character? You have {points} points left\n"))
        points-=brawn
        checker(points)
        defense = int(input(f"What is the defense of your character? You have {points} points left\n"))
        points-=defense
        checker(points)
        if points != 0:
            print("Please make sure you pick numbers that add up to 20 points!")
        else:
            pass
    except:
        print('DUDE.\nOkay freak actually pick a number thats valid.\n')
        

def characters():
    pass

