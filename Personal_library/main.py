#Nicole's Personal Library

music_library = [{
"Dance Away":{
"Artist": "Roxette",
"Album": "Look Sharp",
"Year": 1988,
"Genre": "Rock"
},
"Heavens On Fire":{
"Artist": "Kiss",
"Album": "Smashes Thrashes & Hits",
"Year": 1988,
"Genre": "Rock"
},

}]


def check():
    for key in music_library[0].items():
        for key in music_library[0].items():
            if key != song:
                not_there = True
            elif key == song:
                not_there = False
                break
            
        if not_there == True:
            return 'go ahead'
        elif not_there == False:
            num=+1
            new_song = song + f'({num})'
            print(new_song)
            return new_song


def add(): #Function adds a song to the library
    song = input("What is the song name? ").title()
    artist = input("Who is the artist? ").title()
    album = input("What is the album that it is from? ").title()
    try:
        year = int(input("What year did it come out?:  "))
    except ValueError:
        print("Choose a valid NUMBER.")
        return 'error'

    genre = input(f"What is the genre of {song} by {artist}?: ").title()
    empty = {
    song:{
"Artist": artist,
"Album": album,
"Year": year,
"Genre": genre
},
}
 for key in music_library[0].items():
        for key in music_library[0].items():
            if key != song:
                not_there = True
            elif key == song:
                not_there = False
                break
            
        if not_there == True:
            music_library[0].update(empty)
            print(f'{song} by {artist} has been successfully added to your library!')
        elif not_there == False:
            num=+1
            new_song = song + f'({num})'
            print(new_song)

       
    elif check(song) != 'go ahead':
        empty = {
    check(song):{
"Artist": artist,
"Album": album,
"Year": year,
"Genre": genre
},
}   


    
    
    


def remove(): #Funtion removes a song from the library
    song = input("What is the title of what you would wish to remove? ").title()
    artist = input(f"Who is {song} by?: " ).title()
    for key, value in music_library[0].items():
        if key == song and value["Artist"] == artist:
            del music_library[0][key]
            print("The song was sucessfully removed.")
            return
    print("An error occurred. The song was either not found or was not removed properly.")

        

def display(): #funtion displays the library unless theres nothing there
    if len(music_library) == 0:
        print("There is nothing in your music library currently.")
    else:
        choice = input("""Would you like a simple list or a detailed list: 
(simple or detailed)
""")
        if choice == 'simple':
            print("__________________________________________")
            for key, value in music_library[0].items():
                print(key)
                print("Artist:", value['Artist'])
                print("Album:", value['Album'])
                print("__________________________________________")
        elif choice == 'detailed':
            print("__________________________________________")
            for key, value in music_library[0].items():
                print(key)
                print("Artist:", value['Artist'])
                print("Album:", value['Album'])
                print("Year:", value['Year'])
                print("Genre:", value['Genre'])
                print("__________________________________________")

def search(): #Function searches for a title or artist
    look_for = input("Enter the song title or artist to search for: ").title()
    found = []
    print("__________________RESULTS___________________")
    for key, value in music_library[0].items():
        if not(key == look_for or value['Artist'] == look_for or value['Album'] == look_for or value['Year'] == look_for or value['Genre'] == look_for):
            print("No results.")
        elif key == look_for or value['Artist'] == look_for or value['Album'] == look_for or value['Year'] == look_for or value['Genre'] == look_for:
            print(key)
            print(music_library[0][key])
            print('')
    print("______________________________________________")

    
    

def main(): #Works as the user interface.
    print("Welcome to the music library!")
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

