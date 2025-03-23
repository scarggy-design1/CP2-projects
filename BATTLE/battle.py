import time
import random
from health_bar import plot_health_bars, plt  # Import the health bar plotting function
from damage import randomiz as randomizer, calc as calculate_damage
from load import save_characters, save_monsters

def battle(user_character, monster, characters, monsters):
    print(f"\nBATTLE START!\n----------------\n")
    x = random.randint(1,2)

    stat_user, stat_monster = randomizer(user_character, monster)

    #Now calculate the damage using the randomly selected stats
    user_damage = calculate_damage(user_character, monster, stat_user, stat_monster)
    monster_damage = calculate_damage(monster, user_character, stat_monster, stat_user)
    if x == 1: #decides which character gets to go first based on chance
        print(f"{user_character['name']} attacks first!")
        first_attacker = 'user'
    elif x == 2:
        print(f"{monster['name']} attacks first!")
        first_attacker = 'monster'

    plt.ion()  # Interactive mode on
    user_max_health = user_character['health']


    while user_character['health'] > 0 and monster['health'] > 0: #Main loop that does the battle with switching turns
        plot_health_bars(user_character['health'], user_max_health)
        time.sleep(2)
        if first_attacker == 'user':
            calculate_damage(user_character, monster, stat_user, stat_monster)
            user_damage = calculate_damage(user_character, monster, stat_user, stat_monster)
            monster['health'] -= user_damage
            print(f"\nGOODNESS\n{user_character['name']} attacks {monster['name']} and dealt {user_damage} damage!")
            print(f"{monster['name']} has {monster['health']} health left.")
            time.sleep(3) #Pauses for 3 seconds before continuing execution
            if monster['health'] <= 0:
                print(f"--------------------\n{monster['name']} DEFEATED! {user_character['name']} wins!\n--------------------")
                user_character['level'] += 1  #levels up monster
                save_characters(characters) #saves data
                break
            
            calculate_damage(monster, user_character, stat_monster, stat_user)
            monster_damage = calculate_damage(monster, user_character, stat_monster, stat_user)
            user_character['health'] -= monster_damage
            print(f"\nLOOK AT THAT!!!\n{monster['name']} attacks {user_character['name']} for {monster_damage} damage!")
            print(f"{user_character['name']} has {user_character['health']} health left.")
            time.sleep(2)
            if user_character['health'] <= 0:
                print(f"--------------------\n{user_character['name']} has been DEFEATED! {monster['name']} wins!\n--------------------")
                monster['level'] += 1  #levels up character
                save_monsters(monsters)  #saves data
                print(f'{monster['name']} is now {monster['level']}!')
                break
            
        else:
            calculate_damage(monster, user_character, stat_monster, stat_user)
            monster_damage = calculate_damage(monster, user_character, stat_monster, stat_user)
            user_character['health'] -= monster_damage
            print(f"\nYIKES!!!\n{monster['name']} attacks {user_character['name']} for {monster_damage} damage!")
            print(f"{user_character['name']} has {user_character['health']} health left.")
            time.sleep(2)
            if user_character['health'] <= 0:
                print(f"--------------------\n{user_character['name']} has been DEFEATED! {monster['name']} wins!\n--------------------")
                monster['level'] += 1  #levels up character
                save_monsters(monsters)  #saves data
                break

            calculate_damage(user_character, monster, stat_user, stat_monster)
            user_damage = calculate_damage(user_character, monster, stat_user, stat_monster)
            monster['health'] -= user_damage
            print(f"\n...GET A LOAD OF THIS GUY!\n{user_character['name']} attacks {monster['name']} and dealt {user_damage} damage!")
            print(f"{monster['name']} has {monster['health']} health left.")
            time.sleep(2) #Pauses for 2 seconds before continuing execution
            if monster['health'] <= 0:
                print(f"--------------------\n{monster['name']} DEFEATED! {user_character['name']} wins!\n--------------------")
                user_character['level'] += 1  #levels up monster
                save_characters(characters) #saves data
                break
    plt.ion
    plt.show()  # Keep the plot displayed when the battle ends
    time.sleep(10)
    plt.close()
        

