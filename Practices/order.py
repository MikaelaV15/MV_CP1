#MV 1st order up practice 
#Make a dictionary list 
start = False  
menu_burgers = {
    "bacon Mcdouble": 3.19,
    "Big Mac" : 4.99,
    "Double Quarter Pounder with cheese" : 6.89,
    "Quarter pounde with cheese bacon" : 6.19,
}

menu_drinks = {
    "Soda": 2.98,
    "Slushie" : 3.87,
    "Smoothie" : 4.69,
    "Coffee" : 1.99
}
menu_sides = {
    "Large Fries" : 3.99,
    "Cheese Curds" : 4.78,
    "Nacho Fries" : 5.89,
    "Mozzarella sticks" : 7.43,
    "Onion rings" : 2.89,
    "Mashed potatoes" : 4.75,
    "Mac and cheese" : 3.99
}

order = {}
#Intoduce the user to the code 
start = int(input("Hello welcome to Python Cafe if you want to order press 1 if you don't want to order press 2:"))
if start == 1:
    start = True
if start == 2:
    start = False 
    print("Have a nice day!")
while start == True:
    while True:
        for key, value in menu_burgers:
            print(f"{key}: {value}")
        order = input(f"What would you like to order out of the menu burgers?")
        if order not in menu_burgers:
            print("Not an option...")
        else:
            for key, value in menu_drinks:
                 print(f"{key}: {value}")
            order = input(f"What drink would you like out of menu drinks?")
            if order not in menu_drinks:
                print("That isn't a drink on the menu")
                for key, value in menu_sides:
                    print(f"{key}: {value}")
                order = input(f"What sides would you like to order from menu sides?")
                if order not in menu_sides:
                    print("That is not on the menu_sides")

#Let the user order 
