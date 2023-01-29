import random




class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    
def lanch_Nuke(): # everything is mesured in Km unless stated otherwise # contains updated version 
    print("Lanched Nuke")
    nuke = projectile("Nuke",5,(0,0),1,5)
    nuke.totalMoves = -1 
    do = True
    while do == True: 
            do == True
            if nuke.totalMoves < 0: 
                nuke.totalMoves = nuke.totalMoves + 1
                currentPos = (0,0) 
            elif nuke.totalMoves == 1: 
                currentPos = (1150,2000) 
            elif nuke.totalMoves == 2 :
                currentPos = (2750,4000) 
            elif nuke.totalMoves == 3: 
                currentPos = (5150,4500)
            elif nuke.totalMoves == 4: 
                currentPos = (6700,2000)
            elif nuke.totalMoves == 5:
                currentPos = (7850,30)
                     
            if nuke.totalMoves > 5: 
                print("boom")
                break; 
            else:   
                    print(nuke.totalMoves)       
                    print("Name = " + nuke.name)
                    print("Current Move = %d" % (nuke.totalMoves))
                    print("Pos = (%d,%d)" % (currentPos))
                    print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
                    print("The Blast Raduis = %d" % (nuke.blastRadius))              
                    print("\nNot Exiting\n")

def lanch_General_Purpose_Missle(): # everything is mesured in Km unless stated otherwise

    print("general_Purpose_Misslee")
    gPM = projectile("general Purpose Missle",5,(0,0),1)
    gPM.totalMoves = -1 
    do = True
    while do == True:
            do == True
            if gPM.totalMoves < 0:
             gPM.totalMoves = gPM.totalMoves + 1
             currentPos = (0,0) 
            elif gPM.totalMoves == 1: 
                currentPos = (1150,2000) 
            elif Gpm.totalMoves == 2 :
                currentPos = (2750,4000) 
            elif Gpm.totalMoves == 3: 
                currentPos = (5150,4500)
            elif Gpm.totalMoves == 4: 
                currentPos = (6700,2000)
            elif Gpm.totalMoves == 5:
                currentPos = (7850,30)
                     
            if Gpm.totalMoves > 5: 
                print("boom")
                break; 
            else:        
                    print(Gpm.totalMoves)       
                    print("Name = " + Gpm.name)
                    print("Current Move = %d" % (Gpm.totalMoves))
                    print("Pos = (%d,%d)" % (currentPos))
                    print("Total Projectiles = %d" %  (Gpn.numberOfProjectile) )                
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
        lanch_Nuke()
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

def current_Objects():
     print("Empty")

def current_Info():
     print(move_Counter)

# is the move system of the game and will also be the games main loop  

move_Counter = 0 
do = False # on and off switch for game loop

if coin_toss() == False:
        move_Counter = move_Counter + 1
else: 
        do == True
        move_Counter = move_Counter + 2
while do == True:
    if move_Counter % 2 == 1:
            move_Counter = move_Counter + 1
            print("PlayerOnes Turn")
            current_Info()
            player_One_Choice()
    else: 
            move_Counter = move_Counter + 1
            print("Skip Move\n")
    if move_Counter % 2 == 0: # if odd 
            move_Counter = move_Counter + 1
            print("PlayerTwo Turn")
            current_Info()
            player_Two_Choice()
    else: 
            move_Counter = move_Counter + 1
            print("Skip Move\n")


