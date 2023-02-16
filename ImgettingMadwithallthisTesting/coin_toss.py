import random 
def coin_toss(): # Ran First Starts the Game, and is a 50 50 shot wether playerOne or playerTwo will be ran 
    coin = (random.randint(0,1))
    if coin == 0:
        print("coin_toss\nmove_Counter = 0 ") # Remove Later
        move_Counter = 0 
    else:
        print("coin_toss\nmove_Counter = 1 ") # Remove Later
        move_Counter = 1 
    return move_Counter