#This is lizzy saldanas geometry calc
from shapes import *

def shape(x): #Gets the info for the shape based on parameter
    if x == 'square':
        try:
            s = int(input("What is the side length of your square?: "))
            if s*s == 0: #If any value is 0, it will make this if statement true
                print("You cannot have 0 as a value.")
                return
            choice = input("Which operation would you like done?:\n1) area\n2) perimeter\n3) Both\n")
            square = Square(s)
            
            if choice == '1':
                print(f"The area of your shape is: {square.area()}")
                return
            elif choice == '2':
                print(f"The Perimeter of your square is: {square.perimeter()}")
                return
            elif choice == '3':
                print(f"The Perimeter of your square is: {square.perimeter()}")
                print(f"The area of your square is: {square.area()}")
                return
        except:
            print("Choose a valid choice. Try again. ")
    elif x == 'circle':
        try:
            r = int(input("What is the radius of your circle?: "))
            if r*r == 0:#If any value is 0, it will make this if statement true
                print("You cannot have 0 as a value.")
                return
            choice = input("Which operation would you like done?:\n1) area\n2) perimeter\n3) Both\n")
            circle = Circles(r)
            
            if choice == '1':
                print(f"The area of your circle is: {circle.area()}")
                return
            elif choice == '2':
                print(f"The Perimeter of your circle is: {circle.perimeter()}")
                return
            elif choice == '3':
                print(f"The Perimeter of your circle is: {circle.perimeter()}")
                print(f"The area of your circle is: {circle.area()}")
                return
        except:
            print("Choose a valid choice. Try again. ")
    elif x == 'rectangle':
        try:
            l = int(input("What is the length of your Rectangle?: "))
            w = int(input("What is the width of your Rectangle?: "))
            if l*w == 0:#If any value is 0, it will make this if statement true
                print("You cannot have 0 as a value.")
                return
            rect = Rectangle(l,w)
            choice = input("Which operation would you like done?:\n1) area\n2) perimeter\n3) Both\n")
            if choice == '1':
                print(f"The area of your Rectangle is: {rect.area()}")
                return
            elif choice == '2':
                print(f"The Perimeter of your Rectangle is: {rect.perimeter()}")
                return
            elif choice == '3':
                print(f"The Perimeter of your Rectangle is: {rect.perimeter()}")
                print(f"The area of your Rectangle is: {rect.area()}")
                return
        except:
            print("Choose a valid choice. Try again. ")
    elif x == 'triangle':
        try:
            b = int(input("What is the base of your triangle?: "))
            h = int(input("What is the height of your triangle?: "))
            s = int(input("What is the first side length of your triangle?(not the base): "))
            ss = int(input("What is the second side length of your triangle?(not the base): "))
            if b*h*s*ss == 0:#If any value is 0, it will make this if statement true
                print("You cannot have 0 as a value.")
                return
            choice = input("Which operation would you like done?:\n1) area\n2) perimeter\n3) Both\n")
            tri = Triangle(b,h,s,ss)
            
            if choice == '1':
                print(f"The area of your triangle is: {tri.area()}")
                return
            elif choice == '2':
                print(f"The Perimeter of your triangle is: {tri.perimeter()}")
                return
            elif choice == '3':
                print(f"The Perimeter of your triangle is: {tri.perimeter()}")
                print(f"The area of your triangle is: {tri.area()}")
                return
        except:
            print("Choose a valid choice. Try again. ")