# MV 1st Lists Notes 

sibs = ["Juan","Mika", "Cupid", "YumYum", "Niko", "Cooper"]

print(sibs[1])
print(f"The list is {len(sibs)} people long")
print(sibs)
sibs[0] = "Luis"
sibs[5:-1] = ["Cooper", "YumYum"] 
sibs.pop()
sibs.pop(1)
sibs.remove("Niko")
#sibs.clear()
#sibs.append("Andrew") adds to the end of the list 
sibs.insert(1)