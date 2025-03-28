

def calc(target): #Calculates how to get the target amount with the minmum amount of coins
    """Needs to start with the one highest amount in the csv file
    then once that number gives 0 and its int form, go to the next highest, etc etc
    """
    pass
    

def coins(country): #Gets the target amount and the coins
    try:
        target = int(input('What is your target amount?: '))
    except:
        print("CHOOSE A NUMBER DOOD.")

    if target <= 0: 
        print("Remember. No NEGATIVE numbers or 0!")
        return
    elif target > 0:
        with open('CoinChange\coins.csv', 'r') as file:
            #Get the specific information for this country they picked.
            calc(target)
