import time
import csv

def view_asset(row):
    assets = {
        "Checkings": row[4],
        "Salary": row[5],
        "Goal": row[6],
        "Savings": row[7],
        "House": row[8],
        "Utilities": row[9],
        "Insurance": row[10],
        "Food": row[11],
        "Entertainment": row[12],
        "Healthcare": row[13],
        "Phone": row[14],
        "Pet": row[15]
    }
    print("\nHere are your available assets to choose from.\n---------------\n")
    asset_names = input('1) checkings\n2) salary\n3) goal\n4) savings\n5) house\n6) utilities\n7) insurance\n8) food\n9) entertainment\n10) healthcare\n11) phone\n12) pet\n13) all')
    if asset_names == '1':
        print(f"Checkings: ${value['Checkings']}\n")
    elif asset_names == '2':
        print(f"Salary: ${value['Salary']}\n")
    elif asset_names == '3':
        print(f"Goal: ${value['Goal']}\n")
    elif asset_names == '4':
        print(f"Savings: ${value['Savings']}\n")
    elif asset_names == '5':
        print(f"House: ${value['House']}\n")
    elif asset_names == '6':
        print(f"Utilities: ${value['Utilities']}\n")
    elif asset_names == '7':
        print(f"Insurance: ${value['ChecInsurancekings']}\n")
    elif asset_names == '8':
        print(f"Food: ${value['Food']}\n")
    elif asset_names == '9':
        print(f"Enterainment: ${value['Enterainment']}\n")
    elif asset_names == '10':
        print(f"Healthcare: ${value['Healthcare']}\n")
    elif asset_names == '11':
        print(f"Phone: ${value['Phone']}\n")
    elif asset_names == '12':
        print(f"Pet: ${value['Pet']}\n")
    elif asset_names == '13':
        for asset, value in assets:
            print(f"{asset}: ${value}\n")
    time.sleep(3)
    return

def create_new_account(user):
    password = input("Enter your new password: ")
    checkings = float(input("How much is in your checkings account right now?:\n"))
    salary = float(input('How much do you make per year?:\n'))
    goal = float(input("What is your GOAL? (If you don't have one, input 0):\n"))
    savings = float(input("How much do you have in SAVINGS? (If you don't have any, input 0):\n"))
    house = float(input("How much money do you spend on HOUSE fees every year?:\n"))
    utilities = float(input("How much do you spend on UTILITIES every year?:\n"))
    insurance = float(input("How much do you spend on INSURANCE every year?:\n"))
    food = float(input("How much do you spend on FOOD per year?:\n"))
    entertainment = float(input("How much do you spend on ENTERTAINMENT per year?:\n"))
    healthcare = float(input("How much do you spend on HEALTHCARE every year?:\n"))
    phone = float(input("What is your PHONE bill per year?:\n"))
    pet = float(input("How much do you spend on PET related items per year?:\n"))

    with open('function/finacial_data.csv', 'a') as file: #Use a instead of w so it doesn't delete all of our data
        writer = csv.writer(file)
        writer.writerow([user, password, checkings, salary, goal, savings, house, utilities, insurance, food, entertainment, healthcare, phone, pet])

    print('account created!\n')
    return