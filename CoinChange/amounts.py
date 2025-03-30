

import csv
import time
def display(result, remaining_target): #Function that displays what was needed.
    if remaining_target == 0:
        print("Coins used to reach the target amount:")
        print("------------------")
        for coin_name, (count, value) in result.items():
            print(f"{count} x {coin_name} worth {value}")
        print('\n')
        time.sleep(3)
        return
    else:
        print(f"Couldn't make the exact amount. Remaining amount: {remaining_target:.2f}")
        print("Coins used:\n-------------------")
        for coin_name, (count, value) in result.items():
            print(f"{count} x {coin_name} worth {value}")
        print('\n')
        time.sleep(3)
        return


def calc(target, coin_values, coin_names):
    sorted_coins = sorted(zip(coin_values, coin_names), reverse=True, key=lambda x: x[0]) #Zip allows us to put 2 things together in a tuple so when we reverse it, the associated values can stay together.
    result = {}
    remaining_target = target 
    for coin_value, coin_name in sorted_coins: #Checks each coin to see how many are needed.
        if coin_value <= remaining_target:
            coin_count = int(remaining_target // coin_value)  # How many of this coin are needed
            result[coin_name] = (coin_count, coin_value)  # Store the count of coins and their value
            remaining_target -= coin_count * coin_value  # Subtract the value of the coins used

        elif coin_value > remaining_target: #If the coin is larger than the amount we need, it will skip it.
            pass
        elif remaining_target == 0:
            break  #Once we reach our target, no need to check anymore

    display(result, remaining_target)#calls onto our helper function to display.
    return


def coins(country):  # Gets the target amount and the coins
    try:
        target = float(input('What is your target amount?: '))
    except ValueError: #Checks to make sure user inputs a number with no symbols
        print("CHOOSE A NUMBER DOOD. (No symbols)")
        return

    if target <= 0:
        print("Remember. No NEGATIVE numbers or 0!")
        return
    elif target > 0:
        with open('CoinChange/coins.csv', 'r') as file: #Opens the CSV to get the country data
            reader = csv.reader(file)
            data = list(reader)
            country_data = None
            for row in data:
                if row[0].lower() == country.lower():
                    country_data = row[1:]  # Get the coin data for this country
                    break

            if country_data is None:
                print(f"Sorry, we don't have data for {country}.") #error handling.
                return

            #Get coin names and values by separating
            coin_names = []
            coin_values = []
            for coin in country_data:
                try:
                    coin_name, coin_value = coin.split('-')  #separates at the '-'
                    coin_names.append(coin_name)  
                    coin_values.append(float(coin_value))  #Convert the value part to a float and appends
                except ValueError:
                    print(f"ERROR. There was an unexpected error with coin data: {coin}")
                    return

            calc(target, coin_values, coin_names)  #gives calc our target, values, and coin names
            return