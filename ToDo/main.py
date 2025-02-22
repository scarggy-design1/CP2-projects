#This is Nicoles to-do list

def entire_list(): 
    with open("ToDo/to_do.txt", "r") as f:
        print("_____________________________________________\n")
        for x in f:
            print(x.strip()) 
        print("_____________________________________________\n")

def add():
    new_task = input("What task would you like to add?: ")
    with open("ToDo/to_do.txt", "a") as f:
        f.write(f"( ) {new_task}\n")

def complete():
    ask = input("What task is complete?: ")
    tasks = []
    
    with open("ToDo/to_do.txt", "r") as f:
        tasks = f.readlines()
    
    with open("ToDo/to_do.txt", "w") as f:
        for task in tasks:
            if f'( ) {ask}' == task:
                task = task.replace("( )", "(X)")
            f.write(task)
    
    print(f"Task '{ask}' marked as complete.")

def delete():
    ask = input("What task would you like to delete?: ")
    tasks = []
    
    with open("ToDo/to_do.txt", "r") as f:
        tasks = f.readlines()
    
    with open("ToDo/to_do.txt", "w") as f:
        deleted = False
        for task in tasks:
            if ask in task:
                print(f"Task '{ask}' deleted.")
                deleted = True
                continue
            f.write(task)
        
        if not deleted:
            print(f"Task '{ask}' not found.")
    
def main():
    while True:
        print("WELCOME TO YOUR TO-DO LIST!!!")
        ask = input("""What would you like to do?: 
                    1. View list
                    2. Complete item
                    3. Add task
                    4. Remove task 
                    5. EXIT
                    """)
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

main()
