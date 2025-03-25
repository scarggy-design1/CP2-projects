#This is Lizzys battle assignment
import random

def calc(attacker, defender, stat_user, stat_monster): #damage calculator + helper function
    increase = random.randint(1,10)
    damage = max(0, attacker[stat_user] - defender[stat_monster] + increase + attacker['level']) #uses the selected stats from randomizer function to calculate damage
    return damage

def randomiz(user_character, monster): #Randomizes the stats used so damage is not the same each time
    #Filters out name so the name will not be filtered in as a stat
    user_stats = {key: value for key, value in user_character.items() if key != 'name' and key != 'level'}
    monster_stats = {key: value for key, value in monster.items() if key != 'name' and key != 'level'}
    stat_user = random.choice(list(user_stats.keys()))  #Using random.choice it selects a random item from the list
    stat_monster = random.choice(list(monster_stats.keys()))
    return stat_user, stat_monster #returns the randomly selected choice for stat