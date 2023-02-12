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

nukes = []
ICBM =  [] 
Locations = ["Capital", "Industry","Radar", "MissleDefense"]
country_picked = False
player_Country = ""

class Projectile:
    def __init__(self, name, xCords, yCords,length, width):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords   
        self.yCords = yCords
        self.length = length
        self.width = width


class Radar:
    def __init__(self, name, xCords, yCords, length, width):
        self.name = name
        self.xCords = xCords
        self.yCords = yCords
        self.length = length
        self.width = width


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
my_projectile = Projectile("Nuke", 105, 100, 110, 100)
my_radar = Radar("Radar 1", 100, 100, 110, 100)

def check_Projectile_Collision(projectile, radar):
    if (projectile.xCords >= radar.xCords) and (projectile.xCords <= radar.xCords + radar.length) and (projectile.yCords >= radar.yCords) and (projectile.yCords <= radar.yCords + radar.width):
        print("Location {} was hit".format(radar.name))
    else:                                                                  
        print("Location {} was not hit".format(radar.name))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


# # is the move system of the game and will also be the games main loop 
# do = False # on and off switch for game loop
# while do == True:
#     if player_Picker() == False:
#         #Instead of Breaking Send to Another Function Or Break To Close program
#         print("\nExiting\n")
#         break; 
#     else: 
#         player_Picker()
#         print("Not Exiting\n")


check_Projectile_Collision(my_projectile, my_radar)