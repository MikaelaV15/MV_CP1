#MV 1st dictionaries notes 

#Key: value pairs 

person = {
    "name": "Xavier", 
    "age": 22,
    "job": "Maverick",
    "siblings": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"]
}


person_two = {
    "name": "Jake",
    "age": 22,
    "job": "NEET",
    "siblings": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"]
}

print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in person(key):
            print(f"{person["name"]} has a sibling named {name}")
    else:
        print(f"{key} is {person[key]}")

print(person_two.values())
person_two["age"] -= 1 
print(person_two.items())
person_two["age"] -= 1 