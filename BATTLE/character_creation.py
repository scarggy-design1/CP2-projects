#This is lizzys battle assignment
import csv
from generator import generate_character as gen

# Helper function to check points validity
def checker(points):
    if points == 0:
        return True
    elif points > 200:
        print('DUDE what the heck man dont input a negative number!! (bro really thought they could cheat...)\n')
        return False
    elif points < 0:
        print('You do not have enough points left! SERIOUSLY dood get your act together.\n')
        return False
    return True



def create(): #Creates characters
    print("Welcome to CREATION...\n")
    ask = input("Would you like to \n1) Make your own character\n2) GENERATE\n").strip()
    if ask == '1': #The user can pick and make their own character
        name = input("What is the name of your character: ")
        points = 200
        print(f"\nYou have {points} points to disperse among 4 skills\nCHOOSE WISELY.\n")
        
        try:
            speed = int(input(f"What is the speed of your character? You have {points} points left\n"))
            points -= speed
            if not checker(points):
                return

            health = int(input(f"What is the health of your character? You have {points} points left\n"))
            points -= health
            if not checker(points):
                return

            brawn = int(input(f"What is the strength of your character? You have {points} points left\n"))
            points -= brawn
            if not checker(points):
                return

            defense = int(input(f"What is the defense of your character? You have {points} points left\n"))
            points -= defense
            if points != 0:
                print("You had points left over kiddo... USE ALL OF THEM (trust me)\n")
                return

        except ValueError:
            print('Invalid input my guy (did u type a letter?). Please enter valid NUMBERS for all skills.')
            return
        level = 1
        entire = {
        'name': name,
        'speed': speed,
        'health': health,
        'brawn': brawn,
        'defense': defense,
        'level': level
    }
    
        with open("BATTLE/characters.csv", "a", newline='') as file:
            fieldnames = ["name", "speed", "health", "brawn", "defense", "level"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(entire)
            return entire
    elif ask == '2': #The user will get a randomly generated character
        name, speed, health, brawn, defense, level = gen()
        entire = {
        'name': name,
        'speed': speed,
        'health': health,
        'brawn': brawn,
        'defense': defense,
        'level': level
    }
        with open("BATTLE/characters.csv", "a", newline='') as file:
            fieldnames = ["name", "speed", "health", "brawn", "defense", "level"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(entire)
        return entire

    
    



