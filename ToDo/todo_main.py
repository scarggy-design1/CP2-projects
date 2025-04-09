#This is Nicoles to-do list

def entire_list(): #displays the whole list
    with open("ToDo/to_do.txt", "r") as f:
        print("LIST: ")
        print("\n---------------------")
        for x in f: #Prints for every line in the TO-DO list
            print(x.strip())
            print("---------------------")


def add(): #adds tasks to the txt file
    new_task = input("What task would you like to add?: ")
    with open("ToDo/to_do.txt", "a") as f: #opens file with append so it adds instead of rewriting the entire thing
        f.write(f"( ) {new_task}\n")

def complete(): #Marks your assignment as complete
    ask = input("\nWhat task is complete?: ").strip() #strip gets rid of unwanted white space at the beginning and/or end
    tasks = []
    
    with open("ToDo/to_do.txt", "r") as f:
        tasks = f.readlines()
    
    with open("ToDo/to_do.txt", "w") as f:
        task_found = False
        for task in tasks:
            if task.strip() == f"( ) {ask}":
                task = task.replace("( )", "(X)") #Changes the empty box( ) to complete (X)
                task_found = True
            f.write(task)
        
        if task_found:
            print(f"\n{ask} marked as complete.")
        else:
            print(f"\n{ask} not found or already completed.")

def delete(): #Deletes the task that you want it to
    ask = input("What task would you like to delete?: ").strip() 
    tasks = []
    
    with open("ToDo/to_do.txt", "r") as f:
        tasks = f.readlines()
    
    with open("ToDo/to_do.txt", "w") as f:
        task_found = False
        for task in tasks:

            if task.strip() == f"( ) {ask}" or task.strip() == f"(X) {ask}": #Finds the task and deletes it
                print(f"Task '{ask}' deleted.")
                task_found = True
                continue 
            f.write(task)
        
        if not task_found:
            print(f"Task '{ask}' not found.")

def main(): #Main user interface
    while True:
        print("\nWELCOME TO YOUR TO-DO LIST!!!")
        ask = input("""What would you like to do?: 
                    1. View list
                    2. Complete item
                    3. Add task
                    4. Remove task 
                    5. EXIT
                    \n""")
        if ask == '1':
            entire_list()
        elif ask == '2':
            complete()
        elif ask == '3':
            add()
        elif ask == '4':
            delete()
        elif ask == '5':
            break

if __name__ == "__mainuser__":
    main()

