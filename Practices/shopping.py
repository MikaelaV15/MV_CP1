# MV 1st Shopping list manager 

shopping = ["chocolate", "apples", "Bread", "takis"]
start = True 

while start == True:
    action = int(input("Pick an option 1-4: If you pick 1 you will add an item from the list, if you pick 2 it will remove an item from your list, if you pick 3 you can view the list and 4 stops the list"))
    if action == 1:
        add = input("Pick what you would like to add to your list")
        shopping.append(add)
        print(f"{add} is now in your list")

    elif action == 2:
        item = input("What would you like to remove")
        shopping.remove(item) 
        print(f"{item} is now gone from your list")
    elif action == 3:
        print("Your list consists of:")
        print(shopping) 
    else:
        print("List says bye-bye")
        start = False 
        
