# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 
# https://www.123calculus.com/en/two-circles-calculator-page-7-60-400.html
# Notes
# Once i get the main game loop working, Start figuring out the balencing and add differnces between the types of projectiles 
#
# For The love of god make sure your flags are accrate 
# 
# Fucking Write Test, Holy shit. Test are imporant. 
# Date Of THE Incident 8:44PM 2/1/2023 
#
# Set_Countrys at the begainnig of the game implemting Coin_Toss to randmoize it 
# Add A pouplation Funtion 
#
import random

nukes = []
ICBM =  [] 
Locations = ["Capital", "Industry","Radar", "MissleDefense"]
country_picked = False
player_Country = ""

class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name, totalMoves, currntPos, numberOfProjectile, blastRadius, eta, owner,destCords):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta
    self.owner = owner
    self.destCords = destCords

class Radar:
    def __init__(self, name, pos,owner):
        self.name = name
        self.pos = pos 
        self.owner = owner


def launch_Nuke(nuke, owner):
    def display_info(): 
        print("\nTotalMove = %d" % nuke.totalMoves)       
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
        print("The Blast Raduis = %d" % (nuke.blastRadius))
        print("Pos = (%d,%d,%d)" % (currentPos))
        print("Owner = " + nuke.owner)
        print("destination pos = (%d,%d,%d)" % (nuke.destCords))

        print("\n")

    print("\nLaunched Nuke")
    x = 500 
    y = 2500 
    z = 5002
    nuke = projectile("Nuke", 5, (0,0,0), 1, 5, 0,owner,(x,y,z))
    positions = [(0,0,0),
                (1150,2000,0), 
                (2750,4000,0),
                (5150,4500,0),
                (6700,2000,0),
                (7850,30,0)
                ]   

    for x in range(nuke.eta, nuke.totalMoves, 1): 
        currentPos = positions[x]
        display_info()    
        test_Player() # For testing purposes 
        # player_Picker() # For the real game 
        nuke.eta = x + 1
        if nuke.eta == nuke.totalMoves:
            print("Nuke\nBoom!")
            # player_Picker() # For the real game 
            test_Player() # For testing purposes 
            break 

def launch_ICBM(ICBM, owner):
    def display_info(): 
          print("\nTotalMove = %d" % ICBM.totalMoves)       
          print("Name = " + ICBM.name)
          print("Current Move = %d" % (ICBM.eta ))
          print("Total Projectiles = %d" %  (ICBM.numberOfProjectile) )  
          print("The Blast Raduis = %d" % (ICBM.blastRadius))
          print("Pos = (%d,%d)" % (currentPos))
          print("Owner = " + ICBM.owner)
          print("destination pos = (%d,%d,%d)" % (ICBM.destCords))

          print("\n")
    print("\nLaunched ICBM")
    x = 250
    y = 50 
    z = 75
    ICBM = projectile("ICBM", 5, (0,0,0), 1, 5, 0,owner,(x,y,z))
    positions = [(0,0),(2500, 850), (4000,1000),(5570,800),(7850,9)]   

    for x in (range(ICBM.eta, ICBM.totalMoves, 1)): 
        currentPos = positions[x]
        display_info()    
        test_Player() # For testing purposes 
        # player_Picker() # For the real game 
        ICBM.eta = x + 1
        if ICBM.eta == ICBM.totalMoves:
            check_Projectile_Collision(ICBM, radar)
            print("ICBM\nBoom!")
            # player_Picker() # For the real game 
            test_Player() # For testing purposes 
            break

# def coin_toss(): # Ran First Starts the Game, and is a 50 50 shot wether playerOne or playerTwo will be ran 
#     coin = (random.randint(0,1))
#     if coin == 0:
#         print("coin_toss\nmove_Counter = 0 ") # Remove Later
#         move_Counter = 0 
#     else:
#         print("coin_toss\nmove_Counter = 1 ") # Remove Later
#         move_Counter = 1 
#     return move_Counter


def player_Picker(): # ran everytime and will choose the player based off a counter 
    move_Counter = 0

    if move_Counter % 2 == 0:
        # if not country_picked:
        #     country_Picker()
        #     country_picked = True
        # player_One_Choice()
        test_Player()
    else:
        # player_Two_Choice()
        test_Player()

owner = "test_Player"
radar = Radar("Radar 1",(250,50,75),owner )

def check_Projectile_Collision(projectile, radar):
    if (projectile.destCords == radar.pos):
        print("Location {} was hit".format(radar.name))
    else:                                                                  
        print("Location {} was not hit".format(radar.name))     
def test_Player(counter=0):
    owner = "test_Player"
    move_Counter = 1
    exit_test = [0,2,0,0,0,0,0]
    for x in range(0,7,1):
        
        if exit_test[x] == 1:
            print("Test 1")
            print("x =",x)
            print("exit test is =",exit_test[x])
            print("Move Counter =",move_Counter)
            move_Counter =  move_Counter + 1
            print("\n")
        elif exit_test[x] == 2:
            print("ICB M")

            ICBM.append(projectile("Nuke", 5, (0,0,0), 1, 5, 0,owner,(0,0,0)))
            launch_ICBM(ICBM[-1],owner)
            move_Counter = move_Counter + 1   
            print(x) 
    

        else:
            print("skip")
            move_Counter = move_Counter + 1   
            print(x) 

        if move_Counter == 4:
            break


# is the   system of the game and will also be the games main loop 
do = False # on and off switch for game loop
while do:
    if player_Picker() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        do = False
    else: 
        print("Not Exiting\n")
        do = False

launch_ICBM(ICBM[-1],owner)
