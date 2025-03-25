#This is Lizzys battle assignment
from faker import Faker
import random

fake = Faker()

def generate_character():
    name = fake.name() #Generates a fake name
    
    while total != 200: #Checks to see if the stats add up to 200 and doesn't stop looping until it does.
        speed = random.randint(1, 100)
        health = random.randint(1, 100)
        brawn = random.randint(1, 100)
        defense = random.randint(1, 100)
        total = speed + health + brawn + defense

    level = 1

    return name,speed,health,brawn,defense,level

