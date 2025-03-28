

def calc(target):
    pass
    

def coins(country):
    target = int(input('What is your target amount?: '))
    if target <= 0: 
        print("Remember. No NEGATIVE numbers or 0!")
        return
    elif target > 0:
        with open('CoinChange\coins.csv', 'r') as file:
            #Get the specific information for this country they picked.
            calc(target)
