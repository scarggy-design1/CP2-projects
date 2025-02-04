#Nicoles stuff, notes about dictionaries

car = {
    "Make": "Ford",
    "Model": "Escape xlt",
    "Year": 2008,
    "Color": "Red"
}

print(car["Make"][2])


students = {
    "sixth": {
        1:"Nicole", 
        2:"Luke", 
        3: "Gavin",
        4: "Jackson"

    },
    "First": {
        1: "Hello",
        2: "Evan",
        3: "HE"
    }
}

print(students["sixth"][2])


x = 5

if x == 5:
    print("AYE")
elif x < 6:
    print("AYE")
elif x > 4:
    print("AYE")