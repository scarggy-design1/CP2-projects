#This is Nicole's movie reccomender assignment.

import csv

movies = []
with open("movies/Movies list.csv") as file: #opens the movies csv file.
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)


def entire_thing(): #Prints the entire list of movies
    print("\nFull Movie List:")
    print("_____________________________________________")
    for movie in movies:
        print(f"{movie['Title']}")
        print(f"Rating: {movie['Rating']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Director: {movie['Director']}")
        print(f"Length: {movie['Length (min)']} min")
        print(f"Actors: {movie['Notable Actors']}")
        print("_____________________________________________")



def find(): # Finds movies based on what the user inputs for the criteria
    print("\nWhat kind of movies are you looking for?")

    # Filter options
    genre = input("Enter a genre (leave blank if none): ").strip()
    director = input("Enter a director's name (leave blank if none): ").strip()
    min_length_input = input("Enter a minimum movie length (in minutes, leave blank if none): ").strip()
    max_length_input = input("Enter a maximum movie length (in minutes, leave blank if none): ").strip()
    actors = input("Enter an actor's name (leave blank if none): ").strip()

    # Try to convert min_length_input and max_length_input to integers if they are not empty 
    min_length = None
    max_length = None

    if min_length_input:
        try:
            min_length = int(min_length_input)
        except ValueError:
            print("Invalid length input. Please enter a valid number.")
            return  # Exit the function if the input is invalid

    if max_length_input:
        try:
            max_length = int(max_length_input)
        except ValueError:
            print("Invalid length input. Please enter a valid number.")
            return  # Exits the function if the input is invalid

    filtered_movies = []

    for movie in movies:  # Searches for the movies with the criteria provided by user
        if genre and genre.lower() not in movie['Genre'].lower():
            continue
        if director and director.lower() not in movie['Director'].lower():
            continue

        try:
            if max_length is not None or min_length is not None:
                movie_length = int(movie['Length (min)'])

                if min_length and movie_length < min_length:  # Check for minimum length
                    continue
                if max_length and movie_length > max_length:  # Check for maximum length
                    continue
        except ValueError:
            continue  # Skip this movie in case the Length can't be converted to an integer

        if actors and actors.lower() not in movie.get('Notable Actors', '').lower():
            continue

        filtered_movies.append(movie)

    if len(filtered_movies) > 0:  # If the list isn't empty, it will display this
        print("\nHere are your movie recommendations:")
        print("___________________________________________")
        for movie in filtered_movies:
            print(f"Title: {movie['Title']}")
            print(f"Rating: {movie['Rating']}")
            print(f"Genre: {movie['Genre']}")
            print(f"Director: {movie['Director']}")
            print(f"Length: {movie['Length (min)']} min")
            print(f"Actors: {movie['Notable Actors']}")
            print("_________________________________________")
    else:  # If the list is empty, it will display this
        print("\nNo movies found based on your filters. Try again with different options.")



# Main user interface
def main():
    while True:
        print("\nWelcome to the movie recommender! What are you looking for?\n")
        print("1. Get movie recommendation")
        print("2. Print full movie list")
        print("3. Exit")
        choice = input()

        if choice == '1':
            find()
        elif choice == '2':
            entire_thing()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please pick again.")



main() #Starts the program