#THis is lizzy saldanas personal portfolio program
import sys
import os
import time


#Uses os to get the paths to each module so we can assign it to a variable and use it.
morse_path = os.path.abspath('./morse_code')
pass_path = os.path.abspath('./password_generator')
movie_path = os.path.abspath('./movies')
game_path = os.path.abspath('./games')
todo_path = os.path.abspath('./ToDo')
libr_path = os.path.abspath('./Personal_library')


#sys allows for access to the modules and to manage them.
sys.path.insert(0, morse_path)
sys.path.insert(0, pass_path)
sys.path.insert(0, movie_path)
sys.path.insert(0, game_path)
sys.path.insert(0, todo_path)
sys.path.insert(0, libr_path)



#Import of all the main files for the different projects
import main_morse
import pass_main
import movies_main
import game_main
import todo_main
import libr_main



def mainuser(): #Main user interface
    print("-----------\nWELCOME TO LIZZY SALDANA's PERSONAL PORTFOLIO\n-----------\n")
    print("This portfoilio is based on my favorite 6 projects that I did for my coding class!")
    print('Please follow the directions, and pick the number that corresponds with the option you want.\n')
    while True:
        pick = input("What project would you like to view?\n1) Morse Code Translator\n2) Password Generator\n3) Movie Reccomender\n4) Guessing Game\n5) To-Do List\n6) Personal Library\n7) EXIT\n")
        if pick == '1':
            print('NOTE: This project translates from english to morse code,\n and from morse to english. The process was pretty smooth and easy to understand,\n and I learned how to use indexes to get the specific ones from another list and print their values to form a sentence.\n')
            time.sleep(1)
            main_morse.main()
        elif pick == '2':
            print('NOTE: This project creates passwords for you with a given number of characters,\n and however long you want it to be! (At least 8, though).\n This coding process was tough at the time, but taught me how to use try-except handling.\n')
            time.sleep(1)
            pass_main.main()
        elif pick == '3':
            print('NOTE: This code is able to recommend your movies based on multiple selections from the user.\n The process was very logical and took a lot of time and brain power to figure out how to get the things to work but overall it was really fun and made me very proud in the end when it worked. \nWhat I learned from this code was how to write a search function to search through a file to get necessary information, which helped me a lot in my later projects.\n')
            time.sleep(1)
            movies_main.main()
        elif pick == '4':
            print('NOTE: You get to play a simple guessing game!\n It was part of a Simple and Complex games coding project, and my role in the group was team leader.\n The coding process was a bit too easy, but I learned how to integrate separate code into someone elses.\n')
            time.sleep(1)
            game_main.main()
        elif pick == '5':
            print('NOTE: This code is a simple to do list where you can check off and add remove tasks that you need to do.\n This one was very easy to do and is kind of appealing in my opinion because I often used to do lists for everything and I use this code actually on a daily basis.\n This section taught me how to change an update things to text files\n')
            time.sleep(1)
            todo_main.main()
        elif pick == '6':
            print('NOTE: This is a personal library where you can store your favorite songs and access them and search for things in your library.\n The process of this was sort of fun because we had two parts where we started off with a list and then upgraded to a dictionary and tweak a few features.\n This really taught me how to upgrade my code and make my things easier to read and the importance of comments.\n')
            time.sleep(1)
            libr_main.main()
        elif pick == '7':
            print("Thank you!")
            break
        else:
            print("Please pick a VALID choice.\n")

mainuser() #Starts the program