# MV 1st Password strenght checker 
#make a variable to start the while loop 
start = True 
#print what the program is 
print("This will check how strong your password is and give you a score")
while start == True:
    #set the password score to 0 
    score = 0 
    #set the variables checking if they hit the point to no 
    lens = "no"
    up = "no"
    low = "no"
    digit = "no"
    special = "no"

    #ask for password 
    password = input("What is your password: ")
    #Take len() in the code and check that the length is over 8
    length = len(password)
    if length >= 8:
        score += 1 
        lens = "yes"
        #add +1 to score 

    #check for uppercase using isupper()
    #check if true:
    # if true +1 to score 
    for character in password:
        if character.isupper():
            up = "yes"
    if up == "yes":
        score += 1 
        

    #check for lowercase using islower()
    #check if true:
    #if true +1 to score
    for character in password:
        if character.islower():
            low = "yes"
    if low == "yes":
        score += 1 
        

    #check for numbers using isdigit()
        #check if true
        #if true +1 to score 
    for character in password: 
        if character.isdigit():
            digit = "yes"
    if digit == "yes":
        score += 1 
        

    #check for special chracters 

        #if "!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or  ")" in password or "_" in password or "+" in password or "-" in password or "=" in password or "[" in password or "]" in password or "{" in password or "}" in password or "|" in password or ";" in password or ":" in password or "," in password or "." in password or "<" in password or ">" in password or "?"
        #if true +1 to score 
    for character in password: 
        if "!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or  ")" in password or "_" in password or "+" in password or "-" in password or "=" in password or "[" in password or "]" in password or "{" in password or "}" in password or "|" in password or ";" in password or ":" in password or "," in password or "." in password or "<" in password or ">" in password or "?" in password:
            special = "yes"
    if digit == "yes":
        score += 1 

        
# check for score 
    if score == 1:
        print("You scored a 1, that is very weak")
    elif score == 2:
        print("You got a 2, that is very weak")
    elif score == 3:
        print("You got a 3, it is weak fix it")
    elif score == 4:
        print("You scored a 4! it is strong but you can still do better")
    elif score == 5:
        print("Wow, you scored a 5! That's super strong!")
    else: 
        ("Your password sucks")


    start2 = int(input("do you want to check again if yes click 1 if no click 2"))
    if start2 == 2:
        start = False
        print("Bye")