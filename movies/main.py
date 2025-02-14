#This is Nicoles movie reccomender assignment
import csv
movies = {}
with open("movies/Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:




def find():






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