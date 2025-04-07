#Pie chart
import csv
from accounts import create_new_account, view_asset
import matplotlib.pyplot as plt

def pie_charts():
    # Get user data and expense category
    expense, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = get_info()
    
    # Define expense categories
    if expense == 'Budgeting':
        categories = ['Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        expenses = [one, two, three, four, five, six, seven, eight, nine]
    elif expense == 'Services':
        categories = ['Utilities' ,'Insurance', 'food', 'Entertainment','Healthcare','Phone']
        expenses = [one, two, three, four, five, six]
    elif expense == 'All':
        categories = ['Checkings','Salary','Goal','Savings', 'House', 'Utilities', 'Insurance', 'Food', 'Entertainment', 'Healthcare', 'Phone', 'Pet']
        expenses = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
    
    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(expenses, labels=categories, autopct='%1.1f%%')
    plt.title(f"Expense: {expense}")
    plt.show()


def get_info():
    user = input('What is the name you signed up with, or wish to sign up with?:\n').strip()
    
    # Check if the user already exists in the file
    with open('function/finacial_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        # Search for the user
        for row in data:
            if row[0] == user:
                password = input("What is your password?:\n").strip() #If the user exists, check password
                if row[1] == password:
                    print("Login successful!")
                    ask = input('Would you like to get a pie chart of your data?\n1) Yes\n2) No\n').strip()
                    if ask == '1':
                        choice = input('What expense would you like the pie chart for?\n1) Budgeting\n2) Services\n3) ALL\n').strip()
                        if choice == '1':
                            return 'Budgeting', [float(i) for i in row[4:15]]
                        elif choice == '2':
                            return 'Services',[float(i) for i in row[9:14]]
                        elif choice == '3':
                            return  'All', [float(i) for i in row[2:15]]
                        else:
                            print('Please choose a valid choice.\n')
                            return
                    elif ask == '2':
                        option = input("Got it. Would you like to view a specific assest?\n1) Yes\n2) No").strip()
                        if option == '1':
                            view_asset(row)
                        elif option == '2':
                            print("Exiting...\n")
                            return
                else:
                    print("Incorrect password.")
                    return
        #if the user does not exist then ask if they wanna sign up
        print("Account not found.")
        create_account = input("Would you like to create a new account?\n1) Yes\n2) No\n").strip()
        if create_account.lower() == 'yes':
            create_new_account(user)
            get_info()
            
        elif create_account.lower() == 'no':
            print("Got it. Exiting...\n")
            return
        else:
            return
        

get_info()