#This is Nicole's simple game functions
import random

def one_ten():
    current = 0
    streak = 0
    comp_num = random.randint(1,10)
    while True:
        try:
            user_num = int(input("Guess a number from 1-10!"))
            if user_num >= 1 and user_num <= 10:
                pass
            else:
                continue
        except ValueError:
            print("Please choose a valid NUMBER.")
            continue
        if user_num == comp_num:
            streak=+1
            current=+1
            score = streak*current
            play = input("Would you like to keep playing?(yes or no) ").title()
            if play == 'No':
                return score, 'end'
            elif play == 'Yes':
                return 'again'
        elif user_num != comp_num:
            print("Nope! Try again!")
            streak = 0
            continue


def one_hundred():
    current = 0
    streak = 0
    comp_num = random.randint(1,100)
    while True:
        try:
            user_num = int(input("Guess a number from 1-100!"))
            if user_num >= 1 and user_num <= 100:
                pass
            else:
                continue
        except ValueError:
            print("Please choose a valid NUMBER.")
            continue
        if user_num == comp_num:
            streak=+1
            current=+1
            score = streak*current
            play = input("Would you like to keep playing?(yes or no) ").title()
            if play == 'No':
                return score, 'end'
            elif play == 'Yes':
                return 'again'
        elif user_num != comp_num:
            print("Nope! Try again!")
            streak = 0
            continue