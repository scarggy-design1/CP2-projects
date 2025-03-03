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

def word_count(file):
    number_of_words = 0
    with open(file,'r') as f:
        data = f.read()
        lines = data.split()
    number_of_words += len(lines)
    return number_of_words

def add():
    print("\nWhat is the file's relative path?: ")
    print("The choices you have for file paths are:\n  word_counter/doc.txt\n  word_counter/other_doc.txt\n  or type in the format of word_counter/[INSERT NAME OF THE FILE].txt and it will be created")
    file = input('')
    new = input("What would you like to add?: ")
    with open(file, "a") as f: #opens file with append so it adds instead of rewriting the entire thing
        f.write(f"{new}\n")
    
    with open(file, 'a') as f:
        words = word_count(file)
        f.write(f"  {words} word(s) at {timestamp()}")



        