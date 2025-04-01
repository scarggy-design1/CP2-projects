#Pie chart
import csv
import matplotlib.pyplot as plt
def pie_charts():
    one, two, three, four, five,  six, seven, eight, nine, ten, eleven, twelve, expense = get_info()
    if expense == 'Budgeting':
        x = 'House'
        y = 'Insurange'
        z = 'Utility'
        a = 'Food'
        b = 'Entertainment'
        c = 'Car'
        d = 'Phone'
        e = 'Pet'
    elif expense == '[other thing]':
        pass
    elif expense == '[other thing]':
        pass
    elif expense == '[other thing]':
        pass
    elif expense == '[other thing]':
        pass


    labels = x, y, z, a, b, c, d, e
    sizes = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
    

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)

    plt.show()


def get_info():
    user = input('What is the name you signed up with, or wish to sign up with?:\n')
    password = input("What is your password?:\n")
    with open('function/finacial_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        user_data = None
        for row in data:
            if row[0] == user:
                if row[1] == password:
                    ask = input('Would you like to get a pie chart of your data?\n1) Yes\n2) No\n')
                    if ask == '1':
                        choice = input('What expense would you like the pie chart for?\n1) Budgeting\n2) Services\n3) ALL\n')
                        if choice == '1':
                            expense = 'Budgeting'
                            return expense
                        elif choice == '2':
                            expense = 'Services'
                            return expense
                        elif choice == '3':
                            expense = 'All'
                            return expense
                elif row[1] != password:
                    print("INCORRECT PASSWORD")
                    return

    #If the user already exists, then check for password validity, If the user does not exist, then sign them up.)
    try:
        bank = float(input("How much is in your bank account right now?:\n"))
        salary = float(input('\nHow much do you make per year?:\n'))
        goal = float(input("\nWhat is your GOAL? (If you don't have one, input 0):\n"))
        savings = float(input("\nHow much do you have in SAVINGS? (If you don't have any, input 0):\n"))
        utilities = float(input("\nHow much do you spend on UTILITIES every year?:\n")) #Add an option where they can input per month then just multiply by 12
        insurance = float(input("\nHow much do you spend on INSURANCE every year?:\n"))
        food = float(input("\nHow much do you spend on FOOD per year?:\n"))
        entertainment = float(input("\nHow much do you spend on ENTERTAINMENT per year?:\n"))
        house = float(input("\nHow much money do you spend on HOUSE fees every year?:\n"))
        healthcare = float(input("\nHow muhc do you spend on HEALTHCARE every year?:\n"))
        phone = float(input("\nWhat is your PHONE bill per year?:\n"))
        pet = float(input("\nHow much do you spend on PET related items per year?:\n"))
    except:
        print("CHOOSE A VALID ANSWER. TRY AGAIN")
        return

    pass