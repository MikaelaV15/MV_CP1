# MV 1st String methods

# Stupid/Idiot proofing inputs
color = input("What is your favorite color?").strip().capitalize()
# lower() => all lower case 
# upper() => all uppercase
# capitalize() => capitalize first letter of each word
# title() => czpitalizes the first letter of each word
full_name = input("What is your full name?")
print("That is cool "+ full_name +". I like" + color + "too !")
print("That is cool {full_name}. I like {color} too!" .format(full_name=full_name,color=color))

#F-strings 
print(f"That is cool {full_name}. I like {color} too!") 

pi = "3.14159" 
#print(f"We all know pi is equal to {pi:.3f}")
print(pi.isdecimal()) 


sentence = "The quick brown fox jumps over the lazy dog" 

start = sentence.index("lazy")
length = len("lazy")
print(sentence[start:start+length]) 
