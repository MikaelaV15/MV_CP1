# MV 1st Doors final 
#MV 1st Doors Final Game 


#import random for the rooms
import random 
#start is True 
win = False

#Introduce the user to the game 
    #print("Welcome to doors! this is an adventure horror game")
start = print("Welcome to doors! This is a textbase adventure horror game")
    #Give the instuccions of how the game works 
start = print("in this game you will need to get through 50 doors all different and you will need to watch out for monsters and hints, You will need to survive until door 50 to complete the game if you die there is no coming back. Good luck :)")
start == print("These are the objects in the game")
doors_objects = {
        "Bandages" : "+20 health", 
        "Flashlights" : "safety when light turns off",
        "Candles" : "safety when lights turn off",
        "Keys" : "To unlock next room",
        "Food" : "+5 health", 
        "Cross" : "safety from monsters",
        "papers" : "Hints at keys in door 50",
        "lockpick" : "Replaces key",
        "vitamins" : "+5 health", 
    }


def entrance(items):
            key = int(input("Which key would you like to pick 1-3?"))
            if key == 1:
                print("wrong key try again")
            if key == 2: 
                        print("You got it the door unlocked")
            if key == 3:
                    print("wrong key try again")


def hallway(items):
    print("In this hallway you have found a 3 drawer wardrobe which drawer would yoy like to open?")
    drawer = int(input("pick a drawer 1-3"))
    if drawer == 2:
        print("you got a bandaid")
    if drawer == 2: 
        ("ROAR! the monster bit you")
        user_stats == print(45/50)
    if drawer == 3:
        print("aww you found nothing :|")
        def room1(items):
            print("The door is locked find the key")
            check = int(input("if you would like to check the room press 1 or 2 for thecloset"))
            if check == 1:
                print("You found the key on the ground")
                print("chk chk...oh no..")
                whoops = int(input("There are 2 doors with different numbers which would you like to pick one or two"))
                if whoops == 2:
                    print("it unlocked! good choice")
                if whoops == 1:
                    print("oh no timmothy attacked you")
                    user_stats = print(35/50)
            if check == 2:
                print("oh no there is nothing")
                return hallway(items)
print(doors_objects)
user_stats = print("your beginning health is 50/50") 
user_speed = print("your beginning speed is 10/10")

starts = int(input("to play press 3: "))
if starts == 3:
    while win == False:
        entrance("key")
        hallway("drawer", "check", "whoops")

def room2(items): 
    print("This room has a bed and a closet, would you like to explore?")
    wander = int(input("Press 1 to wander or press 2 to continue to the next room"))
    if wander == 1: 
        item = int(input("press 6 to explore the bed or press 7 to explore the closet... you can only pick one ;)"))
        if item == 6: 
            print("YOU FOUND A CROSS! THATS EXTRA LEGENDARY YOU CAN USE THIS ON A MONSTER TO CHAIN THEM")
        if item == 7: 
            print("There is nothing Womp Womp :)")
            
def room3(items): 
    monster = int(input("would you like to explore? press 1 if yes press 2 to move through"))
    if monster <= 3: 
        rush = int(input("Oh no, the lights are flickerign press 10 to go to the closet press 67 to hide in the wardrobe"))
        if rush == 10: 
            print("YAY, YOU SURVIVED WOOHOOO")
        if rush == 67: 
            print("NOO MY DEAR FRIEND YOU DIED!")


def room4(items):
        print("this room is empty :)")


def room5(items): 
    locked_door = int(input("this room is locked press 76 to check the bed and 89 to check the closet to find the key"))
    if locked_door == 89:
        check = int(input("To check the bed now press 99"))
        if check == 99: 
            locked = int(input("Good job.. you found a lockpick press 3 to use it"))
            if locked == 3:
                print("Great job lets move on")
            if locked_door == 76: 
                locked = int(input("Good job.. you found a lockpick press 3 to use it"))
                if locked == 3: 
                    print("great job lets move on")


def room6(items): 
    hallway_locked = int(input("You are now in a hallway that has a locked door.. press 3 to go left, press 100 to turn right or press 45 to go straight ahead"))
    if hallway_locked == 3:
        beds = int(input("there is a bed a drawer and a typewriter press 1 to search the bed press 8 to checck the drawer and 67 to check the typewriter "))
        if beds == 1: 
            print("theres nothing there")
            check = int(input("press 8 to check the drawer and 67 to check the typewriter"))
            if check == 8: 
                print("theres nothing there")
                check_again = int(input("press 67 to check the typewriter"))
                if check_again == 67: 
                    print("there's nothing there..")
        if beds == 8:
            print("theres nothing there") 
            check = int(input("press 1 to check the bed and 67 to check the typewriter"))
            if check == 1: 
                print("theres nothing there")
                check_again = int(input("press 67 to check the typewriter"))
                if check_again == 67: 
                    print("there's nothing there..")
        if beds == 67: 
            print("There's nothing there..")
            check = int(input("press 1 to check the bed and 8 to check the drawer"))
            if check == 1: 
                print("theres nothing there")
                check_again = int(input("press 8 to check the drawer"))
                if check_again == 8: 
                    print("there's nothing there..")
        if hallway_locked == 100: 
            typewriter = int(input("This room has a bed and a wardrobe press 45 to check the bed or press 60 to check the wardrobe beware you can only pick one.."))
            if typewriter == 60: 
                print("oh no there is nothing there..")
            if typewriter == 45: 
                print("youuu are out of luckkk its empty")


    #define room6(items) 
        #this is a hallway with other rooms and the door is locked 
        #which way you you like to turn? left, right, or straight ahead?
            #if user says left 
                #This room has a bed a drawer and a type writer which would you like to search?
                    #if user says bed 
                        #print(There is nothing there)
                    #if user says drawer 
                        #print(there is nothing there) 
                    #if user says typewriter 
                        #print(There is nothing there)
                #make it so once they pick one they can pick another one 
            #once user has searched everything give it the option to move to another room 
            #if user says right 
                #This room has a wardrobe and a bed which one would you like to search? 
                    #if user says wardrobe
                        #print(There is nothing there)
                    #if user says bed 
                        #print(there is nothing there) 
            #once the user has checked everything give it the option to move on to the next room 
            #Take user to the next room 
                #This room has a wardrobe a box a desk and a drawer 
                    #if user says wardrobe 
                        #print(there is a bandaid would you like to use it?)
                        #if user says yes +20 health 
                        #if user says no make the user check the next part 
                    #if user says desk 
                        #print there is a flashlight would you like to use it?
                        #if user says yes out it in inventory
                    #if user says drawer 
                        #print(there is nothing there)
                    #if user says box 
                        #you found the key go unlock the door 
                #once the user unlocks the door continue to the next part 

    #define room7(items)
        #this room has a monster dont look into its eyes dont turn your head to the left 
            #ask the user which way they would like to go 
                #if user says right 
                    #move on into the next room
                #if user says forward 
                    #move onto the next room
                #if user says backward
                    #move onto the next room 
                #if user says left 
                    #You died 
    #define room8(items) 
        #You have reached the outdoors you are now in the courtyard you have to find a metal key in order to get back in
            #which way would you like to go? (Left, right, or forward?)
            #if the user says right 
                #You find a chest but its locked 
                    #ask the user what way they want to go next     
            #if user says left 
                #you found a lockpick would you like to pick it up?
                    #if user says yes place it in the inventory 
                            #ask the user if they still want to look for the key
                    #if user says no ask it what way then want to go next
            #if the user says forward 
                #congrats you found the key press 2 to pick it up 
                    #would you like to unlock the door now or explore?
                        #if user says unlock the door take it to the door
                        #if the user says explore take them to the arch 
                            #welcome to the arch here you can find vitamins would you like them?
                                #if user says yes give them +5 speed
                                #if user says no take them to unlock the room


#define the CHASE
        #user walks in normally 
            #once user reaches the last 1/3 tell them a screeching noise appears 
                #show (Oh no you have reached the door with SEEK!)
            #the user starts running 
            #oh no the bookshelf fell press 2 to crouch 
                #if user crouches keep running 
                #if user does not crouch 
                    #show (oh no seek caught up to you, bye bye)
            #Oh my there is a closet in the way press 4 to turn right 
                #if user presses 4 keep running 
                #if the user presses another number 
                    #show (oh no seek caught you... bye bye)
            #The end... or so you think 
            #There is fire up ahead press 7 to turn left 
                #if user presses 7 the chase finishes
                #if user presses another number 
                    #show (oh no seek caught you..bye bye)
        #if user survives all obstacles 
            #Show (You survived the chase lets go to the next room)

#Make a function for the final obstacle 
#show : Wow, great job you have made it to door 50, you will have to collect 4 keys in order to escape...This room is like a garage and a monster will be in here... when the monster is near you must stop moving. The keys will be hidden in drawers or just on the ground.. good luck and dont get caught


    #Ask the user what way they would like to go every time 
    #make it so the monster appears once in a while and the user has to stop moving 
    #Make it so if the user moves the user dies 
    #after the user collects all keys the must quietly go unlock the door 
    #If they get caught they die 
    #make dead ends where the user can die 
    #once the user makes it out they will get the award 
    #if the user died ask them to play again 

    #once user wins give them a trophy of achievement 
    #ask them to play