#This is Nicoles notes for reading files
import csv

with open("NOTES/test.txt", "r") as file:
    content = file.read()

users = {}

with open("NOTES/user_info.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.update({row[0]:row[1]})


    