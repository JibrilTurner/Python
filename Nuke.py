# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 

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

class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius,eta):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta

class Country:
    def __init__(self, name, population, xCords,yCords):
        self.name = name
        self.population = population
        self.xCords = xCords
        self.yCords = yCords

class Capital(Country):
    def __init__(self, name, population,xCords,yCords):
        super().__init__(name, population, xCords, yCords)

class Industry(Country):
    def __init__(self, name, workers,xCords,yCords):
        super().__init__(name, 0, xCords, yCords)
        self.workers = workers

class Radar(Country):
    def __init__(self, name, workers, xCords,yCords, radius, power):
        super().__init__(name, workers, xCords, yCords)
        self.radius = radius
        self.power = power 
        self.workers = workers

class MissleDefenseSystem(Country):
    def __init__(self, name, workers, xCords,yCords, radius, power):
        super().__init__(name, workers, xCords, yCords)
        self.radius = radius
        self.power = power 
        self.radius = radius
        self.workers = workers

def set_cuba():
    def display_info():
        print("\ndisplay_info")
        print("\nCountry name:", cuba.name,"\nCountry population:", cuba.population,"\nCountry Xcords:", cuba.xCords,"\nCountry Ycords:", cuba.yCords)
        print("\nCapital name:", moscow.name,"\nCapital population:", moscow.population,"\nCapital Xcords:", moscow.xCords,"\nCapital Ycords:", moscow.yCords)
        print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory Xcords:", factory.xCords,"\nfactory Ycords:", factory.yCords)
        print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)
        print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense Xcords:", missleDefense.xCords,"\nmissleDefense Ycords:", missleDefense.yCords)

    for x in range(0, 4, 1):
        Xcords = int(input("\nset_Country\nEnter X Cords For %s: " % Locations[x]))
        Ycords = int(input("set_Country\nEnter Y Cords For %s: " % Locations[x]))
        cuba = Country('cuba', 60000, 500, 275)
        if Locations[x] == "Capital":
            moscow = Capital('Moscow', 60000, Xcords, Ycords)
        elif Locations[x] == "Industry":
            factory = Industry("Bomb Factory", 5000, Xcords, Ycords)
        elif Locations[x] == "Radar":
            radar = Radar("Radar", 5000, Xcords, Ycords, 50, 1)
        elif Locations[x] == "MissleDefense":
            missleDefense = MissleDefenseSystem("MissleDefense", 2000, Xcords, Ycords, 25, 1)  
            display_info()
    
def set_america():
    def display_info():
        print("\ndisplay_info")
        print("\nCountry name:", america.name,"\nCountry population:", america.population,"\nCountry Xcords:", america.xCords,"\nCountry Ycords:", america.yCords)
        print("\nCapital name:", washington.name,"\nCapital population:", washington.population,"\nCapital Xcords:", washington.xCords,"\nCapital Ycords:", washington.yCords)
        print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory Xcords:", factory.xCords,"\nfactory Ycords:", factory.yCords)
        print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)
        print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense Xcords:", missleDefense.xCords,"\nmissleDefense Ycords:", missleDefense.yCords)
        
    for x in range(0, 4, 1):
        Xcords = int(input("\nset_Country\nEnter X Cords For %s: " % Locations[x]))
        Ycords = int(input("set_Country\nEnter Y Cords For %s: " % Locations[x]))
        global america,washington,factory,radar,missleDefense
        america = Country('USA', 60000, 500, 275)
        if Locations[x] == "Capital":
            washington = Capital('washington', 60000, Xcords, Ycords)
        elif Locations[x] == "Industry":
            factory = Industry("Bomb Factory", 5000, Xcords, Ycords)
        elif Locations[x] == "Radar":
            radar = Radar("Radar", 5000, Xcords, Ycords, 50, 1)
        elif Locations[x] == "MissleDefense":
            missleDefense = MissleDefenseSystem("MissleDefense", 2000, Xcords, Ycords, 25, 1)  
            display_info()


def display_america(): 
    global america, washington, factory, radar, missleDefense
    print("\ndisplay_info")
    print("\nCountry name:", america.name,"\nCountry population:", america.population,"\nCountry Xcords:", america.xCords,"\nCountry Ycords:", america.yCords)
    print("\nCapital name:", washington.name,"\nCapital population:", washington.population,"\nCapital Xcords:", washington.xCords,"\nCapital Ycords:", washington.yCords)
    print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory Xcords:", factory.xCords,"\nfactory Ycords:", factory.yCords)
    print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)
    print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense Xcords:", missleDefense.xCords,"\nmissleDefense Ycords:", missleDefense.yCords)        
          
            
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

    for x in (range(ICBM.eta, ICBM.totalMoves, 1)): 
        currentPos = positions[x]
        display_info()    
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
do = False # on and off switch for game loop
while do == True:
    if player_Picker() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break; 
    else: 
        player_Picker()
        print("Not Exiting\n")

set_america()
display_america()
