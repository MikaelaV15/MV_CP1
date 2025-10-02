# MV 1st Multiplication table 
many = int(input("How big do you want your table to be? :"))

multiplication = 1 

for num in range(1,many +1):
    number = []
    for i in range(1,13):
       number.append(i*multiplication)
    multiplication += 1
    print(number) 
