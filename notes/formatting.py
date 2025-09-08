# MV 1st fromatting outputs

# How do I write the fromat method?

name = "Jake" 
age = 21 
money = 25.06
percent = 74

print("Hello {}, you are {}. That is so old! You have you $ {: .2f} you must be rich!".format(name, age, money))

print (f"Hello {name}, you are {age: ,}. That is so old! You have {money : . 2f} you must be rich! Random percent {percent: .1f}. ")
