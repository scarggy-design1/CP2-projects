


import csv

def calc(target, coin_values, coin_names):
    # Zip the coin names and values together, then sort by value in descending order
    sorted_coins = sorted(zip(coin_values, coin_names), reverse=True, key=lambda x: x[0])

    result = {}
    remaining_target = target  # This is the amount we still need to reach

    for coin_value, coin_name in sorted_coins:
        # If the coin value is smaller than or equal to the remaining target
        if coin_value <= remaining_target:
            coin_count = int(remaining_target // coin_value ) # How many of this coin are needed
            result[coin_name] = coin_count  # Store the count of coins used
            remaining_target -= coin_count * coin_value  # Subtract the value of the coins used
        
        elif coin_value>remaining_target:
            pass
        elif remaining_target == 0:
            break  # If we've reached the target, no need to check further


    if remaining_target == 0:
        print("Coins used to reach the target amount:")
        print("------------------")
        for coin_name, count in result.items():
            print(f"{count} x {coin_name}")
        return
    else:
        print(f"Couldn't make the exact amount. Remaining amount: {remaining_target:.2f}")
        print("Coins used:\n-------------------")
        for coin_name, count in result.items():
            print(f"{count} x {coin_name}")
        return

def coins(country):  # Gets the target amount and the coins
    try:
        target = float(input('What is your target amount?: '))
    except ValueError:
        print("CHOOSE A NUMBER DOOD.")
        return

    if target <= 0:
        print("Remember. No NEGATIVE numbers or 0!")
        return
    elif target > 0:
        with open('CoinChange/coins.csv', mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            country_data = None
            for row in data:
                if row[0].lower() == country.lower():
                    country_data = row[1:]  # Get the coin data for this country
                    break

            if country_data is None:
                print(f"Sorry, we don't have data for {country}.")
                return

            # Extract coin names and values
            coin_names = []
            coin_values = []
            for coin in country_data:
                try:
                    coin_name, coin_value = coin.split('-')  # Split the string by '-'
                    coin_names.append(coin_name)  # Append the coin name
                    coin_values.append(float(coin_value))  # Convert the value part to a float and append
                except ValueError:
                    print(f"ERROR. There was an unexpected error with coin data: {coin}")
                    return

            calc(target, coin_values, coin_names)  # Pass coin names and values to calc
            return