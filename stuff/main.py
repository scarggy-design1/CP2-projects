"""#Nicoles stuff, notes about dictionaries

car = {
    "Make": "Ford",
    "Model": "Escape xlt",
    "Year": 2008,
    "Color": "Red"
}

print(car["Make"])


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
}"""

d = {'a': 1, 'b': 2, 'c': 3}

d.update({'d': 4, 'e': 5})
print(d)


d = {'a': 1, 'b': 2, 'c': 3}

d.setdefault('d', 4)
d.setdefault('e', 5)
print(d)

#d.setdefault('d', 4) checks if the key 'd' exists and if it does, it returns the existing value. Otherwise, it adds 'd': 4.
#d.setdefault('e', 5) does the same for the key 'e', adding 'e': 5 since it doesn't exist.
