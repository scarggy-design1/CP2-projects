 #Nicoles Saldana, writing to txt notes

import csv

"""
r = to read the file
w = write on the file (Replaces thhe old file)
w+ = read and write
a = append (adds to the file, doesn't delete them)(create the file if it doesn't exist)
x = create a file
a+ = append and read the file
"""


"""with open("NOTES/test.txt", "a") as file:
    file.write("\nI have changed this file!")"""
#HOW TO READD:
"""with open("NOTES/user_info.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
"""


#HOW TO WRITE
data= [
    {}
]
with open("NOTES/user_info.csv", "a", newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([["silly_username", "Black"],["HELP <ME", "Red"],["Odd one", "Pink"]])

with open("NOTES/user_info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

