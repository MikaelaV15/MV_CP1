#MV 1st Doors Final Game 


#import random for the rooms
import random 
#start is True 
start = True  

#Introduce the user to the game 
    #print("Welcome to doors! this is an adventure horror game")
start = print("Welcome to doors! This is a textbase adventure horror game")
    #Give the instuccions of how the game works 
start = int(input("in this game you will need to get through 50 doors all different and you will need to watch out for monsters and hints, You will need to survive until door 50 to complete the game if you die there is no coming back. Good luck :), Press 3 to continue in the game "))


#Create a list with all the items that the user can obtain during the game 
if start == 3:
    print("These are the objects in the game")
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
print(doors_objects)
#give the user their stats 
user_stats = 50
#health 50/50 
user_speed = 10
#speed 10/10\
print(user_stats)
#track the users stats 
if user_stats + 1:
    print(user_stats)
    #once the user reaches 0 tell the user they died and ask them if they 
if user_stats == 0:
    print("you died bye")
    #want to play again 
if print("you died bye"):
    play = int(input("would you like to play again? Press 1 to play again, press 2 to leave"))
    if play == 1:
        start = True 
    if play == 2: 
        start = False

#Create a function for the rooms 
     #def entrance(items)
        #Print there are 3 keys which one matches the door:
        #if user picks the wrong key they will loose 5 health
        #If user picks the right key they move on to next part

while start == True:

    def entrance(items):
        print("there are three keys which one matches the door")
        key = int(input("Which key would you like to pick 1-3?"))
        if key == 1:
            print("wrong key try again")
            if key == 2: 
                print("You got it the door unlocked")
            if key == 3:
                print("wrong key try again")
                if key == 2: 
                    print("You got it the door unlocked")
        if key == 2: 
                print("You got it the door unlocked")
        if key == 3:
                print("wrong key try again")
                if key == 2: 
                     print("You got it the door unlocked")
                if key == 1: 
                    print("wrong key try again")
                    if key == 2: 
                        print("You got it the door unlocked")


#Make functions for all of the base of the rooms then randomly generate which one pops up

    #make the functions similar but each with different items in it or its own little catch

#Make the part of the code that will randomly generate each of the rooms until the user reaches door 49 
#use random 

    #define the function hallway(items) 
        #print(in this hallway you encountered a wardrobe which drawer would you like to open?)
        #If user picks 2:
            #You got a bandaid!
        #If user picks 1:
            #drawer monster attacks -5 health 
            #print their health 45/50
        #if user picks 3:
            #Nothing!

    #define room1(items)
        #print("The door is locked find the key")
            #Would you like to check the room or the closet?
                #If user says closet:
                    #empty try again 
                #If user says room:
                    #The key is on the ground
        #print("Oh no there are 2 doors one says 3 and one says 2. which one do you want to pick?")
            #if user picks 2:
            #print("It unlocked good choice")
        #if user picks 1:
            #monster(timothy) attcks -10 health 
            #print health 35/50 or 40/50 
            #Option to use bandaid
            #If user uses bandaid +20 health 
            #print health 

    #define room2(items) 
        #Would you like to explore the room it has a bed and a closet.
            #if user says no 
            #continue to next room 
            #if user says yes ask them what they would like to explore you can only choose one
            #if user says bed check under the bed
                #Good job you found a bandaid +20 health 
            #if user says closet 
                #Oh no there is nothing 


    #define room3(items)
    #print(Would you like to explore there is a closet and a wardrobe")
    #if user says yes ask which one 
        #print(Oh no, The lights are flickering where do you want to go?)
            #If user says closet 
                #monster passes by you survived!
            #if user says wardrobe
                #you cant hide there you died
    #if user survives move on to next room


    #define room4(items) 
    #print this room is empty just walk through 


    #define room5(items) 
    #This room has a bed and a closet check to see if you can find the key 
    #If user says closet
        #print(You cant search there you can only hide)
    #if user says bed 
        #Print(Good job you found a lockpick)
    #Ask the user if they would l
    # 
    # ike to use the lockpick 
        #if user says yes unlock the door 
            #if user says no keep looking for key 
                #if user finds key unlock the door 

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
                #This room has a wardrobe a bed and a desk which one would you like to search? 
                    #if user says wardrobe
                        #print(There is nothing there)
                    #if user says bed 
                        #print(there is nothing there) 
                    #if user says desk 
                        #print(There is nothing there)
                #make it so once they pick one they can pick another one 
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