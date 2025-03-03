#This is Nicole's word counter assignment.
from date import time as timestamp

def entire_thing():
    while True: 
        print("\nWhat is the file's relative path?: ")
        print("The choices you have for file paths are:\n  word_counter/doc.txt\n  word_counter/other_doc.txt\n  or type whatever file name. if it doesn't exist, it'll create one. ")
        file = input('')
        with open(file, "a") as f: #creates file if it doesn't already exist
            pass
        if file == None:
            print("-Nothing is here!-")
        else:
            with open(file, 'r') as f:
                print("---------------")
                lines = f.readlines()
                for line in lines:  # Print each line in the file
                    print(line, end='')
                break


def add():
    while True: 
        print("\nWhat is the file's relative path?: ")
        print("The choices you have for file paths are:\n  word_counter/doc.txt\n  word_counter/other_doc.txt\n  or type in the format of word_counter/[INSERT NAME OF THE FILE].txt and it will be created")
        file = input('')
        new = input("What would you like to add?: ")
        with open(file, "a") as f: #opens file with append so it adds instead of rewriting the entire thing
            f.write(f"{new}\n")
            content = f.readlines()
            words = content.split()
            word_count = len(words)
            f.write(f"  {word_count} word(s) at {timestamp()}")
            break

        