from faker import Faker
import random

fake = Faker()

def generate_character():
    # Generate a random name using Faker
    name = fake.first_name()
    
    # Generate random stats that add up to 200
    speed = random.randint(1, 100)
    health = random.randint(1, 100)
    brawn = random.randint(1, 100)
    defense = random.randint(1, 100)
    
    total = speed + health + brawn + defense
    
    while total != 200:
        speed = random.randint(1, 100)
        health = random.randint(1, 100)
        brawn = random.randint(1, 100)
        defense = random.randint(1, 100)
        total = speed + health + brawn + defense
        

    # Check if the stats total is 200
    total_stats = speed + health + brawn + defense
    adjustment = 200 - total_stats
    
    # If the total doesn't add up to 200, adjust the first stat by the difference


    # Random level between 1 and 10
    level = 1

    return name,speed,health,brawn,defense,level

