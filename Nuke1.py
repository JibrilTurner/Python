# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 

import random


class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius,eta):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta




def lanch_Nuke(): # everything is mesured in Km unless stated otherwise # contains updated version 
    def display_info():
        print("TotalMove = %d" % nuke.totalMoves)       
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
        print("The Blast Raduis = %d" % (nuke.blastRadius))
        print("Pos = (%d,%d)\n" % (currentPos))

               
    print("\nLanched Nuke")
    nuke = projectile("Nuke",5,(0,0),1,5,0)

    while nuke.eta <= 5: 
            if nuke.eta == 0 : 
                currentPos = (0,0) 
                nuke.eta = nuke.eta + 1
                display_info()
                player_Choice()
            elif nuke.eta == 1: 
                currentPos = (1150,2000) 
                nuke.eta = nuke.eta + 1
                display_info()
                player_Choice()

            elif nuke.eta == 2 :
                currentPos = (2750,4000) 
                nuke.eta = nuke.eta + 1
                display_info()
            elif nuke.totalMoves == 3: 
                currentPos = (5150,4500)
                nuke.eta = nuke.eta + 1
                display_info()
            elif nuke.totalMoves == 4: 
                currentPos = (6700,2000)
                nuke.eta = nuke.eta + 1
                display_info()

            elif nuke.totalMoves == 5:
                currentPos = (7850,30)
                nuke.eta = nuke.eta + 1
                display_info()    

            if nuke.eta >= 5: 
                print("boom")
                break; 


       
def lanch_General_Purpose_Missle(): # everything is mesured in Km unless stated otherwise

    print("general_Purpose_Misslee")
    gPM = projectile("general Purpose Missle",5,(0,0),1)
    gPM.totalMoves = -1 
    do = True
    while do == True:
            if gPM.totalMoves < 0:
             gPM.totalMoves = gPM.totalMoves + 1
             currentPos = (0,0) 
            elif gPM.totalMoves == 1: 
                currentPos = (1150,2000) 
            elif gPM.totalMoves == 2 :
                currentPos = (2750,4000) 
            elif gPM.totalMoves == 3: 
                currentPos = (5150,4500)
            elif gPM.totalMoves == 4: 
                currentPos = (6700,2000)
            elif gPM.totalMoves == 5:
                currentPos = (7850,30)
                     
            if gPM.totalMoves > 5: 
                print("boom")
                break; 
            else:        
                    print(gPM.totalMoves)       
                    print("Name = " + gPM.name)
                    print("Current Move = %d" % (gPM.totalMoves))
                    print("Pos = (%d,%d)" % (currentPos))
                    print("Total Projectiles = %d" %  (gPM.numberOfProjectile) )                
                    print("\nNot Exiting\n")

def coin_toss(): # Ran First Starts the Game 
    coin = (random.randint(0,1))
    if coin == 0:
        test_output = True
    else:
        test_output = False
    return test_output

def player_One_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerOneChoice\nenter 0 to fail test Or enter 1 to passtest NUKE: "))
    if exit_test == 1:
        print("Test = true")
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output

def player_Two_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerTwoChoice\nenter 0 to fail test Or enter 1 to passtest NUKE: "))
    if exit_test == 1:
        print("Test = true")
        lanch_Nuke()
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output


# is the move system of the game and will also be the games main loop  

move_Counter = 0 

def do_something():
    global move_Counter
    exit_test = int(input("enter 0 to exit Or enter 1 to loop:\n "))
    if exit_test == 1:
        player_Picker()
        test_output = True
    else:
        test_output = False
    return test_output 

def player_Picker():
    global move_Counter
    if move_Counter % 2 == 0:
        current_Player = True
    else: 
        current_Player = False
    return current_Player

def player_Choice():
    global move_Counter
    if player_Picker() == True:
        player_Choice = int(input("Player Choice PlayerOne\nenter 0 to skip\nenter 1 to lanch nuke: "))
        if player_Choice == 0:
            move_Counter = move_Counter + 1       
        elif player_Choice == 1: 
            move_Counter = move_Counter + 1       
            lanch_Nuke()
    else: 
        player_Choice = int(input("Player Choice PlayerTwo\nenter 0 to exit\nenter 1 to loop: "))

do = True # on and off switch for game loop
while do == True:
    if do_something() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break; 
    else: 
        move_Counter = move_Counter + 1
        print(move_Counter)
        player_Choice()
        print("\nNot Exiting\n")

