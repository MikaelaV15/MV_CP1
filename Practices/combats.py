# MV 1st Combat program activity diagram 

import random 

coin = random.randint(1,2)

health = 0 
defense = 0 
damage = 0 
attack = 0 


monster = 30 
monster_defense = 14
monster_damage = 0 
monster_attack = 0 

def monster1(monster_attack, defense):
    damage = monster_attack - defense
    health -= damage 
    return damage 


def player(attack, monster_defense):
    monster_damage = attack - defense
    monster_health -= monster_damage 
    return monster_damage 

print("Welcome to the Combats, here you have to demolish a monster,what class of fighter are you? If you are a fighter press 1, if you are a mage press 2, if you are a rouge press 3")

fighter = int(input("What class fighter are you?: "))

if fighter == 1: 
    print("health = 30")
    print("defense = 14")
    print("attack = 0")
elif fighter == 2:
    print("health = 60")
    print("defense = 28")
    print("attack = 15")
else:
    print("health = 90")
    print("defense = 42")
    print("attack = 30")