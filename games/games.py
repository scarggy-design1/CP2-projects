#This is Nicole's simple game functions
import random

def one_ten():
    current = 0
    streak = 0
    while True:
            comp_num = random.randint(1,2)
            while True:
                try:
                    user_num = int(input("\nGuess a number from 1-10!\n      "))
                    if user_num >= 1 and user_num <= 10:
                        pass
                    else:
                        print("_______\nCHOOSE FROM 1-10\n_______")
                        continue
                except ValueError:
                    print("Please choose a valid NUMBER.")
                    continue
                if user_num == comp_num:
                    print("\n--------------CONGRATTS!!!! YOU DID IT----------------\n")
                    streak+=1
                    if current <= 3 and current > 0:
                        score = streak*current
                        current = 0
                    elif current > 3:
                        score+=1
                        current = 0
                    elif current == 0:
                        ufhwiuehfiuhwiuf
                    while True:
                        play = input(f"SCORE: {score}\nSTREAK: {streak}\nWould you like to keep playing?(yes or no)\n ").title()
                        if play == 'No':
                            return score, 'end'
                        elif play == 'Yes':
                            break
                        elif play != 'Yes' and play != 'No':
                            print("Choose yes or no. ")
                            continue
                    break
                elif user_num != comp_num:
                    print("Nope! Try again!")
                    print("\n")
                    streak = 0
                    current+=1
                    continue


def one_hundred():
    current = 0
    streak = 0
    while True:
            comp_num = random.randint(1,100)
            while True:
                try:
                    user_num = int(input("\nGuess a number from 1-100!"))
                    if user_num >= 1 and user_num <= 100:
                        pass
                    else:
                        continue
                except ValueError:
                    print("Please choose a valid NUMBER.")
                    continue
                if user_num == comp_num:
                    print("--------------CONGRATTS!!!! YOU DID IT----------------")
                    streak+=1
                    current+=1
                    score = streak*current
                    while True:
                        play = input(f"SCORE: {score}\n Would you like to keep playing?(yes or no)\n ").title()
                        if play == 'No':
                            return score, 'end'
                        elif play == 'Yes':
                            break
                        elif play != 'Yes' and play != 'No':
                            print("Choose yes or no. ")
                            continue
                elif user_num != comp_num:
                    print("Nope! Try again!\n")
                    streak = 0
                    continue