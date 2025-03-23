import random
import time
import pandas as pd
from battle import battle as battle_start
from load import load_characters as charact, load_monsters as monst
from stats import plot_character_radar

def main_game():  # Runs the functions from the separate file to make the game run!
    characters = charact()  # Load characters using the updated pandas-based load_characters()
    monsters = monst()  # Load monsters
    
    if not characters or not monsters:
        print("No characters or monsters available to fight.")
        return

    # Load the characters into a DataFrame
    data = pd.read_csv("BATTLE/characters.csv")

    data['max'] = data[['speed', 'health', 'brawn', 'defense']].max(axis=1)
    data['min'] = data[['speed', 'health', 'brawn', 'defense']].min(axis=1)

    # Select only the 'name', 'level', 'max_stat', and 'min_stat' columns
    selected_data = data[['name', 'level', 'max', 'min']]

    # Display the DataFrame as a table with row numbers starting from 1
    selected_data.index += 1  # Adjust the index to start from 1 instead of 0
    print(selected_data)

    try:
        user_choice = int(input("\nSelect your character by number: ")) - 1
        user_character = characters[user_choice]
        plot_character_radar(user_character)
        ask = input("Is this the character you want to pick? (yes or no)")
        if ask == 'yes' or ask == 'Yes':
            pass
        elif ask == 'no' or ask == 'No':
            return
        else:
            print("Please make sure you pick a VALID ANSWER MY GUY")
            return
    except:
        print("\nDOOD. You gotta stick to what's on this list!\n")
        return
    

    monster = random.choice(monsters)
    print(f"\n{monster['name']} appears!\n-FIGHT FOR YOUR LIFE-\n")
    time.sleep(2)
    battle_start(user_character, monster, characters, monsters)
