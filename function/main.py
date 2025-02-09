#this is nicoles function

venue_names = set()  
venue_stages = {}
venue_equipment = {}

def display_venues():
    if venue_names:
        print("_______Venues available:_______")
        for venue in venue_names:
            print(f"- {venue}\n")
    else:
        print("____________________")
        print("No venues available.")

def add_venue():
    venue = input("What is the name of the venue you would like to add?: ").lower()
    venue_names.add(venue)
    print(f"{venue} added!")
    print("")
    stage = input(f"Enter the name of the stage for {venue}!: ").lower()
    venue_stages[venue] = stage
    venue_equipment[venue] = [] 
    print(f"{stage} was added to the {venue}.")

def remove_venue():
    display_venues()
    print("__________________")
    venue = input("Which venue would you like to remove?: ").lower()
    if venue in venue_names:
        venue_names.remove(venue)
        del venue_stages[venue]  
        del venue_equipment[venue]  
        print(f"{venue} and it's information has been removed.")
    else:
        print(f"{venue} was not found.")

def display_stages():
    if venue_stages:
        print("Stages and their venues:")
        print("____________________")
        for venue, stage in venue_stages.items():
            print(f"Venue: {venue} | Stage: {stage}")
    else:
        print("There are no stages yet.")

def add_equipment():
    venue = input("Enter the venue where you want to add equipment: ").lower()
    if venue in venue_names:
        equipment = input("Enter the equipment name to add: ").lower()
        venue_equipment[venue].append(equipment)
        print(f"{equipment} added to venue {venue} successfully! ")
    else:
        print(f"{venue} was not found.")

def remove_equipment():
    venue = input("What Venue would you like to remove from?: ").lower()
    if venue in venue_names:
        equipment = input("Enter the equipment name to remove: ").lower()
        if equipment in venue_equipment[venue]:
            venue_equipment[venue].remove(equipment)
            print(f"Equipment {equipment} removed from {venue} successfully!")
        else:
            print(f"{equipment} was not found at {venue}.")
    else:
        print(f"{venue} was not found.")

def display_equipment():
    if venue_equipment:
        print("Equipment in each venues stage:")
        for venue, equipment in venue_equipment.items():
            stage = venue_stages[venue] 
            if equipment:
                print("______________________________________________")
                print(f"Venue: {venue} | Stage: {stage} | Equipment:")
                for item in equipment:
                    print(f"   - {item}")
            else:
                print("________________________________________________")
                print(f"Venue: {venue} | Stage: {stage} | No equipment")
    else:
        print("No equipment available.")

def venue_main():
    while True:
        choice = input("""
What would you like to do?
1. Add Venue
2. Remove Venue
3. Add Equipment
4. Remove Equipment
5. Display Venues
6. Display Stages
7. Display Equipment
8. Exit
""")
        if choice == '1':
            add_venue()
        elif choice == '2':
            remove_venue()
        elif choice == '3':
            add_equipment()
        elif choice == '4':
            remove_equipment()
        elif choice == '5':
            display_venues()
        elif choice == '6':
            display_stages()
        elif choice == '7':
            display_equipment()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Try again.")

venue_main()