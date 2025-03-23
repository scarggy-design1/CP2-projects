
import csv
def load_characters():  # Loads characters from CSV using pandas
    characters = []
    try:
        # Read the characters CSV file using pandas
        with open("BATTLE/characters.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                characters.append({
                    'name': row['name'],
                    'speed': int(row['speed']),
                    'health': int(row['health']),
                    'brawn': int(row['brawn']),
                    'defense': int(row['defense']),
                    'level': int(row['level']),
                })
    except FileNotFoundError:
        print("No character data found.")
    return characters


def load_monsters(): #Loads the characters from the monster file
    monsters = []
    try:
        with open("BATTLE/monsters.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                monsters.append({
                    'name': row['name'],
                    'speed': int(row['speed']),
                    'health': int(row['health']),
                    'brawn': int(row['brawn']),
                    'defense': int(row['defense']),
                    'level': int(row['level']),
                })
    except FileNotFoundError:
        print("No monster data found.")
    return monsters

def save_characters(characters): #saves data to character csv file
    with open("BATTLE/characters.csv", "w", newline="") as file:
        fieldnames = ['name', 'speed', 'health', 'brawn', 'defense', 'level']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for character in characters:
            writer.writerow(character)

def save_monsters(monsters): #Saves data to monster csv file
    with open("BATTLE/monsters.csv", "w", newline="") as file:
        fieldnames = ['name', 'speed', 'health', 'brawn', 'defense', 'level']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for monster in monsters:
            writer.writerow(monster)