import random
import time
from battle import battle as battle_start
from load import load_characters as charact, load_monsters as monst

def main_game(): #Runs the functions from the separate file to make the game run!
    characters = charact()
    monsters = monst()
    
    if not characters or not monsters:
        print("No characters or monsters available to fight.")
        return

    print("\nAvailable characters:")
    for idx, character in enumerate(characters, start=1):
        print(f"{idx}. {character['name']}")
    try:
        user_choice = int(input("\nSelect your character by number: ")) - 1
        user_character = characters[user_choice]
    except:
        print("\nDOOD. You gotta stick to whats on this list!\n")
        return
    monster = random.choice(monsters)
    print(f"\n{monster['name']} appears!\n-FIGHT FOR YOUR LIFE-\n")
    time.sleep(2)
    battle_start(user_character, monster, characters, monsters)
