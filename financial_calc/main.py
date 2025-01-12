#Nicole Saldana's financial calc

def savings(): #The function that calculates how long it will take to save for a goal in months
    goal = float(input("What is your goal?: "))
    plan = float(input("How much do you plan to save each month for this goal?: "))
    time = goal/plan
    txt = f'To reach your goal of {goal:.2f} dollars it will take you {time} month(s)'
    print(txt)
    
def compound(): #The function to calculate compound interest
    money = float(input("How much money do you have in your compound interest account?: "))
    percent = float(input("What is the percentage of your compound interest?: "))
    interest = percent/100
    time = int(input("How many years do you plan to have your money in for?: "))
    total = money*interest*time+money
    txt = f"You'll have a total of ${total:.2f} at the end of the {time} year(s)"
    print("starting:", f'${money:.2f}')
    print(txt)

def budget(): #The function to divide your income to a reccomended budgeting tactic
    income = float(input("What is your income?: "))
    savings = income*0.2
    entertainment = income*0.2
    food = income*0.3
    home = income*0.3
    print("according to this, your income of", income, " dollars per year, you should budget your money like so: ")
    print("savings: " ,savings,
          "entertainment: ", entertainment,
           "food: ", food,
            "home: ", home)

def sale_price():#this function calculates the sale price after a discount.
    orginal = float(input("What is the full/total price of the item(s) you are buying?: "))
    discount = float(input("What is the discount? "))
    percent_off = discount/100
    price = orginal-orginal*percent_off
    txt = f'The sale price of your item(s) is {price:.2f}'
    print(txt)

def tip_calc(): #Calculates how much a tip would cost, and rings up grand total
    price = float(input("What is the total price?: "))
    percent = float(input("What is the percentage that you would like to tip?: "))
    theTip = percent/100
    total = price+price*theTip
    txt = f'You will be paying a grand total of {total:.2f}, the tip costing {price*theTip:.2f}'
    print(txt)

def main(): #The user interface
    text = """WELCOME TO FINANCIAL CALULATOR!
            What would you like to do?
            1. Goal Saving
            2. Compound Interest calc
            3. Budgetting Allocator
            4. Sale Price Calculator
            5. Tip Calculator
            6. exit
            """
    while True:
        ask = int(input(text))
        if ask == 1:
            savings()
        elif ask == 2:
            compound()
        elif ask == 3:
            budget()
        elif ask == 4:
            sale_price()
        elif ask == 5:
            tip_calc()
        elif ask == 6:
            break
        else:
            print("Invalid choice. Pick again.")

main()