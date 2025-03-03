#This is Nicoles advanced functions notes

"""What is a helper function?
        A function we write to call into another function. Makes functions less bloated and easier to read.
EX:"""

def is_int(user_input):
    try:
        int(user_input)
    except:
        print("PLEASE give me a number.")
        is_int(input("How old are you?\n"))
    return int(user_input)
    
def age():
    old = is_int(input("How old are you?\n"))
    print(f"Cool. You are {old}.")

age()

"""
What is the purpose of a helper function?
    The purpose of a helper function is to make your functions less bloated and make them easier to read.


What is an inner function?
    A function that exists inside of another function."""

def add(a):
    b = int(input("Give me a number: "))

    def addition():
        print(a+b)
    addition()



"""

What is the scope of a variable in a function WITH an inner function?
    The scope is the outer function. Anything that exists within the outer function 
    can be accessed by the inner function, 
    but the stuff inside the inner function cannot be accessed by the outer function

Why do we use inner functions?
    Makes it so you dont have to use as many return statements, also can be used for debugging!!!


What is a closure function?
    Allows a function to remember information across multiple functions. 

"""
def add(a):

    def addition(b):
        return a+b
    return addition


base = add(10)

print(base(5))
"""
Why do we write closure functions?
    It saves and remembers information across multple functions.

What is recursion?
    When we call a function inside of itself.


How does recursion work?
    All it is doing is calling the function inside itself, and giving it new information.


"""