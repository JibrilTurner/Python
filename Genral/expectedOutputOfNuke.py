def do_something():
    exit_test = int(input("DoSmth\nenter 0 to Play Move Or enter 1 to Skip A Move: "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output

def player_One_Choice():
    exit_test = int(input("playerOneChoice\nenter 0 to lauch Nuke Or enter 1 to Suck dick : "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output

def player_Two_Choice():
    exit_test = int(input("playerTwochoice\nenter 0 to lauch Nuke Or enter 1 to Suck dick : "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output


 
# Movecounter = 0 
# do = True
# while do == True:
#     if do_something() == False:
#         Movecounter = Movecounter + 1
#     else: 
#         do == True
#         Movecounter = Movecounter + 1

#     if Movecounter % 2 == 1:
#             print("PlayerOnes Turn")
#             player_One_Choice()
#     else: 
#             print("PlayerOnes Turn")
#             print("Skip Move")

#     if Movecounter % 2 == 0:
#             print("PlayerTwo Turn")
#             player_Two_Choice()
#     else: 
#             print("PlayerTwo Turn")
#             print("Skip Move")







            

# def Playchoice():



class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    


def LanchNuke():
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


def generalPurposeMissle():
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
                currentPos = (1150,2000,) 
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

LanchNuke()