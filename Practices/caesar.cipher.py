#MV 1st period Caesar Cipher 

#Capital ASCII letters start at 65 and end at 90 
#Lowercase letters start at 97 and end at 122
#MV 1st period Caesar Cipher 

#Capital ASCII letters start at 65 and end at 90 
#Lowercase letters start at 97 and end at 122

#A is 65
print(f"A = {ord("A")}")
#B is 66
print(f"B = {ord("B")}")
#C is 67
print(f"C = {ord("C")}")
#D is 68
print(f"D = {ord("D")}")
#E is 69 
print(f"E = {ord("E")}")
#F is 70 
print(f"F = {ord("F")}")
#G is 71
print(f"G = {ord("G")}")
#H is 72
print(f"H = {ord("H")}")
#I is 73
print(f"I = {ord("I")}")
#J is 74
print(f"J = {ord("J")}")
#K is 75
print(f"K = {ord("K")}")
#L is 76
print(f"L = {ord("L")}")
#M is 77
print(f"M = {ord("M")}")
#N is 78
print(f"N = {ord("N")}")
#O is 79
print(f"O = {ord("O")}")
#P is 80 
print(f"P = {ord("P")}")
#Q is 81
print(f"Q = {ord("Q")}")
#R os 82
print(f"R = {ord("R")}")
#S is 83
print(f"S = {ord("S")}")
#T is 84
print(f"T = {ord("T")}")
#U is 85
print(f"U = {ord("U")}")
#V is 86
print(f"V = {ord("V")}")
#W is 87
print(f"W = {ord("W")}")
#X is 88
print(f"X = {ord("X")}")
#Y is 89
print(f"Y = {ord("Y")}")
#Z is 90 
print(f"Z = {ord("Z")}")



#a is 97
print(f"a = {ord("a")}")
#b is 98
print(f"b = {ord("b")}")
#c is 99
print(f"c = {ord("c")}")
#d is 100
print(f"d = {ord("d")}")
#e if 101
print(f"e = {ord("e")}")
#f is 102
print(f"f = {ord("f")}")
#g is 103
print(f"g = {ord("g")}")
#h is 104 
print(f"h = {ord("h")}")
#i is 105
print(f"i = {ord("i")}")
#j is 106
print(f"j = {ord("j")}")
#k is 107
print(f"k = {ord("k")}")
#l is 108
print(f"l = {ord("l")}")
#m is 109
print(f"m = {ord("m")}")
#n is 110
print(f"n = {ord("n")}")
#o is 111
print(f"o = {ord("o")}")
#p is 112
print(f"p = {ord("p")}")
#q is 113
print(f"q = {ord("q")}")
#r is 114
print(f"r = {ord("r")}")
#s is 115
print(f"s = {ord("s")}")
#t is 116
print(f"t = {ord("t")}")
#u is 117
print(f"u = {ord("u")}")
#v is 118
print(f"v = {ord("v")}")
#w is 119
print(f"w = {ord("w")}")
#x is 120
print(f"x = {ord("x")}")
#y is 121
print(f"y = {ord("y")}")
#z is 122
print(f"z = {ord("z")}")

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