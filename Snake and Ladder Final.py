import random
import time

print("                   Snake and Ladder                ")

str(input('''
Rules:
Only 2 Players can play the game.
Snake Bites are at 43,50,56,73,84,87 and 98
Steps are at 2,6,20,52,57 and 71.\n\n'''))


steps={2:23,6:45,20:59,52:72,57:96,71:92}
snake_bite={43:17,50:5,56:8,73:15,87:49,84:58,98:40}
count=[0,0,0,0,0]
player_names={}


def num_of_player_to_play():
    global num_of_player
    try:
        num_of_player=int(input("Enter number of player:"))
        if num_of_player > 4 or  num_of_player < 2:
            print("Enter number of player between 2 to 4")
            return num_of_player_to_play()
        else:
            player()
    except ValueError:
        print("Please enter in digit")
        return num_of_player_to_play()


def player():
    global player_names
    len_player_names=len(player_names)
    for i in range(len_player_names+1,num_of_player+1):
        name=input("Enter the name of {} player :".format(i))
        if name:
            if name in player_names.values():
                print("Duplicare Name not allowed")
                return player()
                break
            else:
                 player_names[i]=name
        else:
             return player()
    else:
        turn()
            

def turn():
    global count
    while True:
        for i in player_names:
            time.sleep(2)
            input("{} Press Enter to roll the dice:".format(player_names[i]))
            dice_rolled=random.randint(1,6)
            print("Rolling...")
            time.sleep(2)
            print("Its ",dice_rolled)
            count[i]=count[i]+dice_rolled
            if count[i] > 100:
                count[i]-=dice_rolled
                time.sleep(2)
                print("{} is on {} step.".format(player_names[i],count[i]))
                time.sleep(2)
                print("{} you are only {} steps away from winning.\n".format(player_names[i],100-count[i]))
            elif count[i] in snake_bite:
                 time.sleep(2)
                 print("Ohhh!!!!,Snake bited you")
                 count[i]=snake_bite[count[i]]
                 time.sleep(2)
                 print("{} Moved to step {}.\n".format(player_names[i],count[i]))
            elif count[i] in steps:
                 time.sleep(2)
                 print("WOW!!! You climbed the steps")
                 count[i]=steps[count[i]]
                 time.sleep(2)
                 print("{} climbed to step {}\n".format(player_names[i],count[i]))
            elif count[i]==100:
                 print("Congratulations {} you have won the game.".format(player_names[i]))
                 new_game()
            else:
                time.sleep(2)
                print("{} Moved from {} step to {} step\n".format(player_names[i],count[i]-dice_rolled,count[i]))
    
def new_game():
    game=input("Do you want to start a new Game(YES/NO):")
    if game=="YES" or game=="yes":
        num_of_player_to_play()
    elif game=="NO" or game=="no":
        exit()
    else:
        print("Please Enter proper input")
        return new_game()
            
num_of_player_to_play()   
  
        
        
       

        
