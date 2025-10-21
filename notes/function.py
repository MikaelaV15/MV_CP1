# MV 1st period funtions notes 
#set variables 
player_health = 100 
monster_health = 100 
#define functions 
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else: 
        return monster_health, player_health - amount 
    
monster_health, player_health = damage(10, "player")
print(f"monster_health: {monster_health}")
print(f"Player_health: {player_health}")
def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names: 
        initials += name[0]
    
    return initials 
total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0 
while x < add(3,9):
    print("duck")
    x+= 1 

print("Goose")
print(initials("Tia Larose"))
print(initials("Franco Barbosa"))

print(f"a = {ord("a")}")
print(f"98 = {chr(98)}")
print(f"b = {ord("b")}")
