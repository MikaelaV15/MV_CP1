#MV 1st Square roots 
#Make the list of a minimum of 20 numbers 
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#Make a function 
new_numbers = map(lambda num:num**2, numbers)
i = 0 
#make a loop 
for nums in new_numbers: 
    print(f"Original {numbers[i]}, Squared Root {nums}")
    i += 1