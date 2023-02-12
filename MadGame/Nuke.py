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
from math import acos, sqrt
my_projectile = []

nukes = []
ICBM =  [] 
Locations = ["Capital", "Industry","Radar", "MissleDefense"]
country_picked = False
player_Country = ""

class Projectile:
    def __init__(self, name, xCords, yCords,length, Width,totalMoves,eta):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.Width = Width
        self.totalMoves = totalMoves
        self.eta = eta 

class Radar:
    def __init__(self, name, xCords, yCords, length, width):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width



def set_cuba():
    def display_info():
        print("\ndisplay_info")
        print("\nRadar name:", radar.name, "\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)

        
    for x in range(0, 4, 1):
        xCords = 500
        yCords = 500
        # Xcords = int(input("\nset_cuba\nEnter X Cords For %s: " % Locations[500]))
        # #  while Xcords > 500:
        #     # Xcords = int(input("X Cords Cannot be greater than 500, Enter X Cords Again: "))
        # Ycords = int(input("Enter Y Cords For %s: " % Locations[500]))
        #     # Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))
        global cuba,havana,factory,radar,missleDefense
        radar = Radar("Radar 1", xCords, yCords, 110, 100)
        if Locations[x] == "Radar":
            radar = Radar("Radar 1", xCords, yCords, 110, 100 )

def set_america():
    def display_info():
        print("\ndisplay_info")
        print("\nRadar name:", radar.name, "\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)


    for x in range(0, 4, 1):
        xCords = 500
        yCords = 500
        # Xcords = int(input("\nset_america\nEnter X Cords For %s: " % Locations[x]))
        # # while Xcords > 500:
        #     # Xcords = int(input("X Cords Cannot be greater than 500, Enter X Cords Again: "))
        # Ycords = int(input("Enter Y Cords For %s: " % Locations[x]))
        # # while Ycords > 500:
        #     # Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))
        global america,washington,factory,radar,missleDefense
        radar = Radar("Radar 1", xCords, yCords, 110, 100)
        if Locations[x] == "Radar":
            radar = Radar("Radar 1", xCords, yCords, 110, 100 )
    
def display_cuba(): 
    print("\ndisplay_cuba")
    print("Country name:", cuba.name,"\nCountry population:", cuba.population,"\nCountry Xcords:", cuba.xCords,"\nCountry Ycords:", cuba.yCords)
    print("\nCapital name:", havana.name,"\nCapital population:", havana.population,"\nCapital Xcords:", havana.xCords,"\nCapital Ycords:", havana.yCords)
    print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory Xcords:", factory.xCords,"\nfactory Ycords:", factory.yCords)
    print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)
    print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense Xcords:", missleDefense.xCords,"\nmissleDefense Ycords:", missleDefense.yCords)   

def display_america(): 

    print("\ndisplay_america")
    print("Country name:", america.name,"\nCountry population:", america.population,"\nCountry Xcords:", america.xCords,"\nCountry Ycords:", america.yCords)
    print("\nCapital name:", washington.name,"\nCapital population:", washington.population,"\nCapital Xcords:", washington.xCords,"\nCapital Ycords:", washington.yCords)
    print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory Xcords:", factory.xCords,"\nfactory Ycords:", factory.yCords)
    print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar Xcords:", radar.xCords,"\nradar Ycords:", radar.yCords)
    print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense Xcords:", missleDefense.xCords,"\nmissleDefense Ycords:", missleDefense.yCords)         

def launch_Projectile():
    print("launch_Projectile 1")

    my_projectile = Projectile("Nuke", 105, 100, 110, 100,5,0)

    print("Name = " + my_projectile.name)
    print("\nTotalMove = %d" % my_projectile.totalMoves) 
    print("eta = %d" % (my_projectile.eta ))
    print("xPos = %d" % (my_projectile.xCords))
    print("yPos = %d2" % (my_projectile.yCords))
    print("\n")

    # \positions = [(0,0),(1150,2000), (2750,4000),(5150,4500),(6700,2000),(7850,30)]   
        # positions = [(0, 0), (1150, 2000), (2750, 4000), (5150, 4500), (6700, 2000), (7850, 30)]\
    ypositions = [(0), (2000),(4000) ,(4500), (100), (100)]
    xpositions = [(0), (2000),(4000) ,(4500), (105), (30)]


    for x in range(0,6,1):
        xCords = xpositions[x]
        yCords = ypositions[x]
        my_projectile.yCords, my_projectile.xCords = yCords, xCords

        # test_Player() # For testing purposes                               
        # player_Picker() # For the real game 
        print("\nTotalMove = %d" % my_projectile.totalMoves) 
        print("eta = %d" % (my_projectile.eta ))
        my_projectile.eta =  my_projectile.eta + 1 
        if my_projectile.eta == my_projectile.totalMoves: 
            print("Nuke xPos = %d" % (my_projectile.xCords))
            print("Nuke yPos = %d" % (my_projectile.yCords))
            print("radar xPos = %d" % (my_radar.xCords))
            print("radar yPos = %d" % (my_radar.yCords))
            check_Projectile_Collision(my_projectile, my_radar)
            print("boom")
            player_Test_Choice() # For the real game 
        #test_Player() # For testing purposes 
            break
                                
def launch_ICBM(ICBM, owner):
    def display_info(): 
            print("\nTotalMove = %d" % ICBM.totalMoves)       
            print("Name = " + ICBM.name)
            print("Current Move = %d" % (ICBM.eta ))
            print("Total Projectiles = %d" %  (ICBM.numberOfProjectile) )  
            print("The Blast Raduis = %d" % (ICBM.blastRadius))
            print("xPos = %d" % (ICBM.xCords))
            print("yPos = %d" % (ICBM.yCords))       
            print("Owner = " + ICBM.owner)
            print("xPos = %d" % (ICBM.xCordsFinal))
            print("yPos = %d" % (ICBM.yCordsFinal))       
            print("\n")

    print("\nLaunched ICBM")
 
    ICBM = projectile("ICBM", 5, 0, 0, 1, 0.5, 0, owner)
    ypositions = [(0),(2500), (4000),(5570),(100)]   
    xpositions = [(0),(850), (1000),(800),(100)]   

    for x in range(ICBM.eta, ICBM.totalMoves): 
        yCords, xCords = ypositions[x], xpositions[x]
        ICBM.yCords, ICBM.xCords = yCords, xCords

        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        ICBM.eta = x + 1
        if ICBM.eta == ICBM.totalMoves:
            check_Projectile_Collision()
            print("ICBM\nBoom!")
            player_Picker() # For the real game 
        #test_Player() # For testing purposes 
            break


def set_ICBM():
        global projectile
        owner = "test"
        Xcords = 500
        Ycords = 500
        projectile("ICBM", 5, Xcords, Ycords, 1, 0.5, 0, owner)

        check_Projectile_Collision()



def intersection_area(d,r1,r2): # finds the area of the intersection of two circles, d = distance between center1 -> r1 and center2 -> r2 = r1 = raduis1 r2 = raduis2   
    d1 = (r1**2 - r2**2 + d**2) / (2 * d)
    d2 = d - d1
    area = (r1**2 * acos(d1/r1) - d1 * sqrt(r1**2 - d1**2)) + (r2**2 * acos(d2/r2) - d2 * sqrt(r2**2 - d2**2))
    return area

def circle_area(r): # finds the area of a circle,  r = raduis  
    area = 3.14 * r**2
    return area 

def coin_toss(): # Ran First Starts the Game, and is a 50 50 shot wether playerOne or playerTwo will be ran 
    coin = (random.randint(0,1))
    if coin == 0:
        print("coin_toss\nmove_Counter = 0 ") # Remove Later
        move_Counter = 0 
    else:
        print("coin_toss\nmove_Counter = 1 ") # Remove Later
        move_Counter = 1 
    return move_Counter

move_Counter = coin_toss() 

def player_Picker(): # ran everytime and will choose the player based off a counter 
    global move_Counter, country_picked
    if move_Counter % 2 == 0:
        if not country_picked:
            country_Picker()
            country_picked = True
        # player_One_Choice()
        player_Test_Choice()

    else:
        # player_Two_Choice()
        player_Test_Choice()
        


def player_Test_Choice(projectile): # choices playerOne can make 
    global move_Counter 
    
    exit_test = int(input("\nplayer_Test_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter 3 to view country info\n Enter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1      
        my_projectile.append(Projectile("Nuke", 105, 100, 110, 100,5,0)) 
        launch_Projectile(my_projectile[-1])

    elif exit_test == 2:
        launch_Projectile()
    elif exit_test == 3: 
        player_One_Stats() 
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        player_Test_Choice()
        move_Counter = move_Counter + 1       

def player_One_Stats(): # displays the stats of playerOne  
    if player_Country == "cuba":
        print("\nplayer_One_Stats\nplayerOne is cuba") 
        display_cuba()
    else:
        print("\nplayer_One_Stats\nplayerOne is america") 
        display_america()

def player_Two_Stats(): # displays the stats of playerTwo  
    if player_Country == "cuba":
        print("\nplayer_Two_Stats\nplayerOne is america") 
        display_america()
    else:
        print("\nplayer_Two_Stats\nplayerTwo is cuba") 
        display_cuba()

def country_Picker(): # Gives the player a choice on what country, player is selceted off the decsion of coin toss 
    global country_picked, player_Country
    if not country_picked:
        if coin_toss() == True: 
            print("\ncountry_Picker\nplayerOne goes first")
            player_choice = int(input("Enter 0 for Cuba\nEnter 1 for America:\nEnter Option: "))
            if player_choice == 0: 
                print("\nplayerOne is now cuba")
                set_cuba()
                print("playerTwo is now america")
                set_america()
                player_Country = "cuba" 
            else: 
                print("\nplayerOne is now america")
                set_america()
                print("playerTwo is now cuba")
                set_cuba()
                player_Country = "america" 
        else: 
            print("\ncountry_Picker\nplayerTwo goes first")
            player_choice = int(input("Enter 0 for Cuba\nEnter 1 for America:\nEnter Option: "))
            if player_choice == 0: 
                print("playerTwo is now cuba")
                set_cuba()
                print("playerOne is now america")
                set_america()
                player_Country = "cuba" 
            else: 
                print("playerTwo is now america")
                set_america()
                print("playerOne is now cuba")
                set_cuba()
                player_Country = "america" 
        country_picked = True

def player_One_Choice(): # choices playerOne can make 
    owner = "player_One"
    global move_Counter 
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter 3 to view country info\n Enter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        Projectile.append(projectile("Nuke", 105, 100, 110, 100,0,5))
        launch_Projectile(Projectile[-1], Projectile)
    elif exit_test == 2:
        set_ICBM()
    elif exit_test == 3: 
        player_One_Stats() 
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1       

def player_Two_Choice(): # choices playerTwo can make 
    owner = "player_Two"
    global move_Counter
    exit_test = int(input("\nplayer_Two_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter 3 to view country info\n Enter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        (projectile("Nuke", 5, 0, 0, 1, 5, 0,owner))


        launch_Nuke(nukes[-1],owner)
    elif exit_test == 2:
        set_ICBM()
    elif exit_test == 3: 
        player_Two_Stats()    
    else:
        print("player_Two_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1      


owner = "Test"
my_projectile = Projectile("Nuke", 105, 100, 110, 100,0,5)
my_radar = Radar("Radar 1", 100, 100, 110, 100)

def check_Projectile_Collision(projectile, radar):
    if (projectile.xCords >= radar.xCords) and (projectile.xCords <= radar.xCords + radar.length) and (projectile.yCords >= radar.yCords) and (projectile.yCords <= radar.yCords + radar.width):
        print("Location {} was hit".format(radar.name))
    else:                                                                  
        print("Location {} was not hit".format(radar.name))
                                                                                                                                                                                                                            

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


# check_Projectile_Collision(my_projectile, my_radar)
set_cuba()
set_america()
player_Test_Choice()
# launch_Projectile("cake")