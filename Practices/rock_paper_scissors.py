# Mv 1st period Rock Paper Scissors 
import random 
win = False 

bot_win = 0 
human_win = 0

while win == False:
    random1 = random.randint(1,3)
    if random1 == 1:
        choice = "rock"
    elif random1 == 2:
        choice = "paper"
    elif random1 == 3:
        choice = "scissors"
    choice2 = int(input("What option would you like to pick?: option 1 is rock, option 2 is paper, option 3 is scissors: "))
    if choice2 == 1:
        choice2 = "rock"
    elif choice2 == 2:
        choice2 = "paper"
    elif choice2 == 3:
        choice2 = "scissors"
    else:
        print(f"{choice2} is not an option try again")


    if choice == "rock" and choice2 == "paper":
        print("The human won, they picked paper and bot picked rock")
        human_win += 1 
    if choice == "rock" and choice2 == "scissors":
        print("The bot won, rock beats scissors")
        bot_win += 1 
    if choice == "rock" and choice2 == "rock":
        print("It's a tie rock doesn't beat rock")
    if choice == "paper" and choice2 == "paper":
        print("It's a tie, paper doesn't beat paper")
    if choice == "paper" and choice2 == "scissors":
        print("The human wins, scissors beats paper")
        human_win += 1 
    if choice == "paper" and choice2 == "rock":
        print("The bot wins, paper beats rock")
        bot_win += 1 
    if choice == "scissors" and choice2 == "paper":
        print("Bot wins, scissors beats paper")
        bot_win += 1 
    if choice == "scissors" and choice2 == "rock":
        print("Human wins, rock beats scissors")
        human_win += 1 
    if choice == "scissors" and choice2 == "scissors":
        print("It's a tie, scissors doesn't beat scissors") 


    print(f"the bot score is : {bot_win}\nthe human score is: {human_win}")

    start = int(input("Do you want to continue if so pick 1, if you want to end pick 2:"))
    if start == 2:
        win = True 