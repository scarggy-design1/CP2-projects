#Nicole saldana, multiple python pages notes

"""
How do you make multiple files in python?
        Just click new file and end it with .py
        snake_case file names descriptive names.
        Keep names short and sweet.

How do you get a function from another file
"""
from calc import add as addition, subtract as sub

print(addition(4,8))
print(sub(8,4))

"""    (* lets me import everything!!)
    alising is where you import a function and give it a new keyword

How do you get variables from another file?
    Just add it to the list, but that way is not good syntax. 
    You want to get a returned version of the variable and call the 
    function on the other page.


How do you have a function with multiple returns?
"""
def get_user_info():
    name = input("What is your name?")
    age = input("What is your age?")
    color = input("What is your favorite color?")
    return name, age, color

name, age, color = get_user_info()

print(age)

"""
Why would you use multiple pages for a python project? 
    Easier to merge on github branches
    Modularity - breaking our program into smaller more managable pieces
    MAIN should only include your introduction and your user interface.
    Functionality - keeps your code clean

    FOR MULTIPLE PAGES:
        if __name__ == "main":
        call function
"""