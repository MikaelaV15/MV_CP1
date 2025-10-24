#MV 1st period Caesar Cipher 

#Capital ASCII letters start at 65 and end at 90 
#Lowercase letters start at 97 and end at 122

#A is 65
print(f"A = {ord("A")}")
print(f"65 = {chr(65)}")
#B is 66
print(f"B = {ord("B")}")
print(f"66 = {chr(66)}")
#C is 67
print(f"C = {ord("C")}")
print(f"67 = {chr(67)}")
#D is 68
print(f"D = {ord("D")}")
print(f"68 = {chr(68)}")
#E is 69 
print(f"E = {ord("E")}")
print(f"69 = {chr(69)}")
#F is 70 
print(f"F = {ord("F")}")
print(f"70 = {chr(70)}")
#G is 71
print(f"G = {ord("G")}")
print(f"71 = {chr(71)}")
#H is 72
print(f"H = {ord("H")}")
print(f"66 = {chr(66)}")
#I is 73
print(f"I = {ord("I")}")
print(f"66 = {chr(66)}")
#J is 74
print(f"J = {ord("J")}")
print(f"66 = {chr(66)}")
#K is 75
print(f"K = {ord("K")}")
print(f"66 = {chr(66)}")
#L is 76
print(f"L = {ord("L")}")
print(f"66 = {chr(66)}")
#M is 77
print(f"M = {ord("M")}")
print(f"66 = {chr(66)}")
#N is 78
print(f"N = {ord("N")}")
print(f"66 = {chr(66)}")
#O is 79
print(f"O = {ord("O")}")
print(f"66 = {chr(66)}")
#P is 80 
print(f"P = {ord("P")}")
print(f"66 = {chr(66)}")
#Q is 81
print(f"Q = {ord("Q")}")
print(f"66 = {chr(66)}")
#R os 82
print(f"R = {ord("R")}")
print(f"66 = {chr(66)}")
#S is 83
print(f"S = {ord("S")}")
print(f"66 = {chr(66)}")
#T is 84
print(f"T = {ord("T")}")
print(f"66 = {chr(66)}")
#U is 85
print(f"U = {ord("U")}")
print(f"66 = {chr(66)}")
#V is 86
print(f"V = {ord("V")}")
print(f"66 = {chr(66)}")
#W is 87
print(f"W = {ord("W")}")
print(f"66 = {chr(66)}")
#X is 88
print(f"X = {ord("X")}")
print(f"66 = {chr(66)}")
#Y is 89
print(f"Y = {ord("Y")}")
print(f"66 = {chr(66)}")
#Z is 90 
print(f"Z = {ord("Z")}")
print(f"66 = {chr(66)}")


#a is 97

#b is 98

#c is 99

#d is 100

#e if 101

#f is 102

#g is 103

#h is 104 

#i is 105

#j is 106

#k is 107

#l is 108

#m is 109

#n is 110

#o is 111

#p is 112

#q is 113

#r is 114

#s is 115

#t is 116

#u is 117

#v is 118

#w is 119

#x is 120

#y is 121

#x is 122



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
        new_char = chr((ord(char) - base + shift) % 26 + base)
        result += new_char
    else: 
        #Leave non-alphabetic characters un touched 
        result += char
    
    return result 

#ask user if they want to encode or decode
def main():
    int(input("Welcome to Caesar Cipher to encode pick 1 to decode pick 2"))
    choice = input()
    if choice == 2:
        print("Welcome to decode")
    else: 
        print("Welcome to encode")