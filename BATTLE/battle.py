import csv
import random

# Helper function to load characters from a CSV file
def load_characters():
    characters = []
    try:
        with open("BATTLE/characters.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                characters.append({
                    'name': row['name'],
                    'speed': int(row['speed']),
                    'health': int(row['health']),
                    'brawn': int(row['brawn']),
                    'defense': int(row['defense']),

                })
    except FileNotFoundError:
        print("No character data found.")
    return characters

# Helper function to load monsters from a CSV file
def load_monsters():
    monsters = []
    try:
        with open("BATTLE/mosters.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                monsters.append({
                    'name': row['name'],
                    'speed': int(row['speed']),
                    'health': int(row['health']),
                    'brawn': int(row['brawn']),
                    'defense': int(row['defense'])
                })
    except FileNotFoundError:
        print("No monster data found.")
    return monsters


def calculate_damage(attacker, defender):
    damage = max(0, attacker['brawn'] - defender['defense'])  # Simple damage calculation
    return damage


def battle(user_character, monster):
    print(f"\nThe battle begins between {user_character['name']} and {monster['name']}!")
    
    # Determine who attacks first based on highest stat
    user_highest_stat = max(user_character, key=user_character.get)  # Compare highest stat
    monster_highest_stat = max(monster, key=monster.get)
    
    if user_character[user_highest_stat] > monster[monster_highest_stat]:
        print(f"{user_character['name']} attacks first!")
        first_attacker = 'user'
    elif user_character[user_highest_stat] < monster[monster_highest_stat]:
        print(f"{monster['name']} attacks first!")
        first_attacker = 'monster'
    else:
        # If tied, speed determines who goes first
        if user_character['speed'] > monster['speed']:
            print(f"{user_character['name']} attacks first due to higher speed!")
            first_attacker = 'user'
        else:
            print(f"{monster['name']} attacks first due to higher speed!")
            first_attacker = 'monster'

    while user_character['health'] > 0 and monster['health'] > 0:
        if first_attacker == 'user':
            damage_to_monster = calculate_damage(user_character, monster)
            monster['health'] -= damage_to_monster
            print(f"\n{user_character['name']} attacks {monster['name']} for {damage_to_monster} damage!")
            print(f"{monster['name']} has {monster['health']} health left.")
            if monster['health'] <= 0:
                print(f"{monster['name']} has been defeated! {user_character['name']} wins!")
                return
            
            # Monster's turn to attack
            damage_to_user = calculate_damage(monster, user_character)
            user_character['health'] -= damage_to_user
            print(f"{monster['name']} attacks {user_character['name']} for {damage_to_user} damage!")
            print(f"{user_character['name']} has {user_character['health']} health left.")
            if user_character['health'] <= 0:
                print(f"{user_character['name']} has been defeated! {monster['name']} wins!")
                return
            
            first_attacker = 'monster'  # Switch turns
        else:
            damage_to_user = calculate_damage(monster, user_character)
            user_character['health'] -= damage_to_user
            print(f"\n{monster['name']} attacks {user_character['name']} for {damage_to_user} damage!")
            print(f"{user_character['name']} has {user_character['health']} health left.")
            if user_character['health'] <= 0:
                print(f"{user_character['name']} has been defeated! {monster['name']} wins!")
                return

            # User's turn to attack
            damage_to_monster = calculate_damage(user_character, monster)
            monster['health'] -= damage_to_monster
            print(f"{user_character['name']} attacks {monster['name']} for {damage_to_monster} damage!")
            print(f"{monster['name']} has {monster['health']} health left.")
            if monster['health'] <= 0:
                print(f"{monster['name']} DEFEATED! {user_character['name']} wins!")
                return
            
            first_attacker = 'user' 

def main_game():
    characters = load_characters()
    monsters = load_monsters()
    
    if not characters or not monsters:
        print("No characters or monsters available to fight.")
        return

    print("\nAvailable characters:")
    for idx, character in enumerate(characters, start=1):
        print(f"{idx}. {character['name']}")
    
    user_choice = int(input("\nSelect your character by number: ")) - 1
    user_character = characters[user_choice]
    monster = random.choice(monsters)
    print(f"\n{monster['name']} appears!\n-FIGHT FOR YOUR LIFE-\n")
    battle(user_character, monster)