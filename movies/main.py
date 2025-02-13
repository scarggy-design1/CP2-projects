#This is Nicoles movie reccomender assignment
import csv
movies = {}
with open("movies/Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        movies.update({row[0]:row[1]})




def find():
    print(movies)
    print()
    ask = input("1. Title\n 2. Director\n 3. Genre\n 4. Rating\n 5. Length (min)\n 6. Notable Actors\n (1-6)")
    ask2 = input("Is there any others that you would like to add to your filter? (yes or no)").title()
    if ask == '1':
        pass
    elif ask == '2':
        pass
    elif ask == '3':
        pass
    elif ask == '4':
        pass
    elif ask == '5':
        pass
    elif ask == '6':
        pass
    else:
        print("Invalid choice.")
    
    if ask2 == 'Yes':
        print("1. Title\n 2. Director\n 3. Genre\n 4. Rating\n 5. Length (min)\n 6. Notable Actors\n")
        add_to = input("(1-6)")
        #Copy and paste ask stuff into this
    elif ask2 == "No":
        pass
    else:
        print("Invalid Choice.")




def main():
    while True:
        print("Welcome to the movie reccomender! What are you looking for?")
        print("1. Get movie reccomendation\n 2. Exit")
        choice = input("")
        if choice == '1':
            find()
        elif choice == '2':
            break
        else:
            print("Invalid Choice, pick again.\n")


main()