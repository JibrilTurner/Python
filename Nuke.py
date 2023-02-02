# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 

# Notes
# Once i get the main game loop working, Start figuring out the balencing and add differnces between the types of projectiles 
#
# For The love of god make sure your flags are accrate 
# 
# Fucking Write Test, Holy shit. Test are imporant 8:44PM 2/1/2023 



import random

class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius,eta):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta

nukes = []
ICBM =  [] 

def launch_Nuke(nuke):
    def display_info(): 
        print("\nTotalMove = %d" % nuke.totalMoves)       
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
        print("The Blast Raduis = %d" % (nuke.blastRadius))
        print("Pos = (%d,%d)\n" % (currentPos))

    print("\nLaunched Nuke")
    nuke = projectile("Nuke", 5, (0,0), 1, 5, 0)
    positions = [(0,0),(1150,2000), (2750,4000),(5150,4500),(6700,2000),(7850,30)]   

    for x in range(nuke.eta, nuke.totalMoves, 1): 
        currentPos = positions[x]
        display_info()    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        nuke.eta = x + 1
        if nuke.eta == nuke.totalMoves:
            print("Nuke\nBoom!")
            player_Picker() # For the real game 
           #test_Player() # For testing purposes 
            break 

def launch_ICBM(ICBM):
    def display_info(): 
          print("\nTotalMove = %d" % ICBM.totalMoves)       
          print("Name = " + ICBM.name)
          print("Current Move = %d" % (ICBM.eta ))
          print("Total Projectiles = %d" %  (ICBM.numberOfProjectile) )  
          print("The Blast Raduis = %d" % (ICBM.blastRadius))
          print("Pos = (%d,%d)\n" % (currentPos))

    print("\nLaunched ICBM")
    ICBM = projectile("ICBM", 5, (0,0), 1, 0.5, 0)
    positions = [(0,0),(2500, 850), (4000,1000),(5570,800),(7850,0)]   

    for i, x in enumerate(range(ICBM.eta, ICBM.totalMoves, 1)): 
        currentPos = positions[x]
        display_info(i+1)    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        ICBM.eta = x + 1
        if ICBM.eta == ICBM.totalMoves:
            print("ICBM\nBoom!")
            player_Picker() # For the real game 
        #test_Player() # For testing purposes 
            break


def coin_toss(): # Ran First Starts the Game 
    coin = (random.randint(0,1))
    if coin == 0:
        print("coin_toss\nmove_Counter = 0 ") # Remove Later
        move_Counter = 0 
    else:
        print("coin_toss\nmove_Counter = 1 ") # Remove Later
        move_Counter = 1 
    return move_Counter

move_Counter = coin_toss() 

def player_Picker():
    global move_Counter
    if move_Counter % 2 == 0:
        player_One_Choice()
    else: 
        player_Two_Choice()


def test_Player(): # Remove Later
    global move_Counter
    exit_test = int(input("\nTest_Player_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_ICBM(ICBM[-1])
    else:
        move_Counter = move_Counter + 1       
        print("Test = false") 

def player_One_Choice():
    global move_Counter
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_Nuke(ICBM[-1])
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1       

def player_Two_Choice():
    global move_Counter
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_Nuke(ICBM[-1])
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1       

# is the move system of the game and will also be the games main loop  


do = True # on and off switch for game loop
while do == True:
    if player_Picker() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break; 
    else: 
        player_Picker()
        print("Not Exiting\n")
