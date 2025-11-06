# MV 1st elif and logical operators notes
begin = True 

grade = int(input("What is your number grade?"))

if grade > 100:
    print(f"You did extra credit... you did {grade -100}% extra credit!") 
elif grade == 100: 
    print(f"Your grade is perfect!")
else: 
    print(f"Try harder you only have {grade}.")
if grade < 100:
    print(f"You are not trying enough a {grade} is for losers")
elif grade == 99:
     print(f"You are so close to a perfect grade")
else:
    print(f"you are so smart a {grade} is for nerds :) ")

start = int(input("Would you like to check your grade for another class? if yes pick 1 if no pick 2"))
if start == 2:
    begin = False 
    print("BYEE")