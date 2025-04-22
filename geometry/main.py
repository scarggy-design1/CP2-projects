#This is lizzy saldanas geometry calc
from info_shapes import *


def main():#Main user interface
    while True:
        y = input("What shape would you like to choose?:\n1) Square\n2) Circle\n3) Rectangle\n4) Triangle\n5) EXIT\n")
        if y == '1':
            shape('square')
        elif y == '2':
            shape('circle')    
        elif y == '3': 
            shape('rectangle')
        elif y == '4':
           shape('triangle')
        elif y == '5':
            break
        else:
            print("Choose a valid choice man. ")

main()

