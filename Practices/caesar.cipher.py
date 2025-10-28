#MV 1st period Caesar Cipher 

#Capital ASCII letters start at 65 and end at 90 
#Lowercase letters start at 97 and end at 122
#MV 1st period Caesar Cipher 


#Welcome to the Caesar Cipher for encode pick 1 for decode pick 2:
def caesar_cipher(text,shift,mode):
    result = ""

#Reverse shift if you are decoding 
    if mode == "decode":
        shift = -shift
    
    for char in text:
        if char.isalpha(): #check if it is a letter 
        #Determine the ASCII base (A or a)
            base = ord("A") if char.isupper() else ord("a")
        #Shift character using wrap 26
        new_char = chr((ord(char) - base + shift) + base)
        result += new_char
    else: 
        #Leave non-alphabetic characters un touched 
        result += char
    
    return result 

#ask user if they want to encode or decode
def main():
    choice = int(input("Welcome to Caesar Cipher to encode pick 1 to decode pick 2: "))
    if choice == 2:
        print("Welcome to decode")
    else: 
        print("Welcome to encode")

