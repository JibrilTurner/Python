import random

class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    
def lanch_Nuke(): # everything is mesured in Km unless stated otherwise
    print("Lanched Nuke")
    nuke = projectile("Nuke",5,(0,0),1,5)
    nuke.totalMoves = -1 
    do = True
    while do == True:
    
        if do_something() == 0:
            print("\nExiting\n")
            break;        
        else: 
            do == True
            nuke.totalMoves = nuke.totalMoves + 1
            currentPos = (0,0) 
            if nuke.totalMoves == 1: 
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

def general_Purpose_Missle(): # everything is mesured in Km unless stated otherwise

    print("Lanched Nuke")
    nuke = projectile("Nuke",5,(0,0),1)
    nuke.totalMoves = -1 
    do = True
    while do == True:
    
        if do_something() == 0:
            print("\nExiting\n")
            break;        
        else: 
            do == True
            nuke.totalMoves = nuke.totalMoves + 1
            currentPos = (0,0) 
            if nuke.totalMoves == 1: 
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
                    print("\nNot Exiting\n")

def do_something(): # Ran First Starts the Game 
    exit_test = (random.randint(0,1))
    print(exit_test)
    if exit_test == 0:
        test_output = True
    else:
        test_output = False
    return test_output

def player_One_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerOneChoice\nenter 0 to fail test Or enter 1 to passtest: "))
    if exit_test == 1:
        print("Test = true")
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output

def player_Two_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerTwochoice\nenter 0 to fail test Or enter 1 to passtest: "))
    if exit_test == 1:
        print("Test = true")
        lanch_Nuke()
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output


# is the move system of the game and will also be the games main loop  
Movecounter = 0 
do = True
while do == True:
    if do_something() == False:
        Movecounter = Movecounter + 1
    else: 
        do == True
        Movecounter = Movecounter + 2

    if Movecounter % 2 == 1:
            print("PlayerOnes Turn")
            player_One_Choice()
    else: 
            print("PlayerOnes Turn")
            print("Skip Move\n")

    if Movecounter % 2 == 0: # if odd 
            print("PlayerTwo Turn")
            player_Two_Choice()
    else: 
            print("PlayerTwo Turn")
            print("Skip Move\n")
