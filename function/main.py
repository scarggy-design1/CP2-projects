#this is nicoles function



def display_venue():
    pass
    
def venue_add():
   ask = input("What is the name of the venue you would like to add?: ")
   time = input(f"What times are available for the {ask}?")
   venue = (ask, time)



def venue_remove():
    display_venue()
    ask = input("What venue would you like to remove?: ")


def equipment_status():
    ask = input("Would you")



def display_equipment():
    pass

def venue_main():
    while True:
        choice = input("""What would you like to do?:
1. Add Venue names
2. Remove Venue names
3. Add equipment
4. Remove equipment
5. Change status of equipment
6. Display Venue
7. Display equipment and status
8. Exit
                        """)
        if choice == '1':
            venue_add()
        elif choice == '2':
            venue_remove()
        elif choice == '3':
            'BLANK'
        elif choice == '4':
            'BLANK'
        elif choice == '5':
            equipment_status()
        elif choice == '6':
            display_venue()
        elif choice == '7':
            display_equipment()
        elif choice == '8':
            break
        else:
            pass


venue_main()