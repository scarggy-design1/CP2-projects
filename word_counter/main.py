#This is Nicole's word counter assignment.


from file import entire_thing as display, add as add_item

def main():
    while True:
        ask = input("""\nWhat would you like to do?
                    1) write on file
                    2) read file
                    3) exit
                    """)
        if ask == '1':
            add_item()
        elif ask == '2':
            display()
        elif ask == '3':
            break

main()
