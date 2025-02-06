#Nicole's Personal Library

music_library = [("Dance Away", "Roxette",), ("Play That Funky Music", "Wild Cherry"), ("I've Had Enough(Into the Fire)", "Kiss"),
("Zanzibar", "Billy Joel"), ("Physical Fasination", "Roxette"), ("The Look", "Roxette")]

#    genre = input(f"What is the genre of {song} by {artist}?: ")
    
def add(): #Function adds a song to the library
    song = input("What is the song name? ").title()
    artist = input("Who is the artist? ").title()

    music = (song, artist)
    music_library.append(music)
    print(f'{song} by {artist} has been successfully added to your library!')

def remove(): #Funtion removes a song from the library
    song = input("What is the title of what you would wish to remove? ").title()
    artist = input(f"Who is {song} by?" ).title()
    music = (song, artist)
    music_library.remove(music)
    if music in music_library:
        print("It was not removed successfully.")
    else: 
        print(f'{song} by {artist} has been sucessfully removed.')

def display(): #funtion displays the library unless theres nothing there
    if len(music_library) == 0:
        print("There is nothing in your music library currently.")
    else:
        print(music_library)

def search(): #Function searches for a title or artist
    look_for = input("Enter the song title or artist to search for: ").title()
    found = []
    for song, artist in music_library:
        if look_for in song or look_for in artist:
            found.append((song, artist))
    if found:
        print("________RESULTS:___________")
        for song, artist in found:
            print(f"FOUND: {song} by {artist}\n")
            print("___________________________")
    else:
        print(f"No matching songs or artists found for '{look_for}'.")
    
    

def main(): #Works as the user interface.
    display()
    while True:
        print('')
        question = input("""What would you like to do?: 
                        1. add to library
                        2. remove from library
                        3. display library
                        4. search
                        5. exit
                         """)
        if question == '1':
            print('')
            add()
        elif question == '2':
            print('')
            remove()
        elif question == '3':
            print('')
            display()
        elif question == '4':
            print('')
            search()
        elif question == '5':
            break
        else:
            print('')
            print("invalid choice! Pick again.")

main()

