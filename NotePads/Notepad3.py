import random
import math
from math import acos, sqrt

class projectile:
    def __init__(self, name,totalMoves,currntPos,endPos,eta,owner ):
        self.name = name
        self.totalMoves = totalMoves
        self.currntPos = currntPos 
        self.endPos = endPos 
        self.eta = eta
        self.owner = owner

    def display_Nuke(self):
        print("\ndisplay_Nuke")
        print("TotalMove = %d" % nuke.totalMoves)       
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Pos = (%d,%d,%d)" % (nuke.currntPos))
        print("End Pos = (%d,%d,%d)" % (nuke.endPos))
        print("Owner = " + nuke.owner)
        print("\n")

nuke_list = []
move_Counter = 1 


def parametricEqu(currntPos, endPos, angle):
    x0, y0, z0 = currntPos
    x1, y1, z1 = endPos
    # calculates the initial velocity and angle(Radiens) Dont feel like converting to degrees 
    vx = math.sqrt((x1 - x0) * 9.81 / (2 * math.sin(math.pi / angle))) 
    vy = vx * math.sin(math.pi / angle)

    # calculate time of flight
    t = (x1 - x0) / vx

    # calculate y coordinates for each time step
    steps = 4  # number of time steps
    dt = t / steps
    y_coords = []
    z_coords = []
    traj_coords = []
    for i in range(steps + 1):
        t_i = i * dt
        y = y0 + vy * t_i - 0.5 * 9.81 * t_i ** 2
        y_coords.append(y)
        z = z0 + (z1 - z0) * t_i / t
        z_coords.append(z)

        # store current (x, y, z) coordinates in traj_coords array
        x = x0 + i * (x1 - x0) / steps
        traj_coords.append((round(x, 2), round(y, 2), round(z, 2)))

    return traj_coords    

def launch_Nuke(nuke, currntPos, endPos, angle):
    print("\nLaunched Nuke")
    positions = parametricEqu(currntPos, endPos, angle)
    for x in range(0, 5, 1):
        print(positions[x])

    nuke_list.append(nuke)
    for x in range(nuke.eta, nuke.totalMoves, 1):
        for nuke in nuke_list:
            nuke.currentPos = positions[x]
            nuke.eta = nuke.eta + 1
            ProgramBody()  # For the real game
            if nuke.eta == nuke.totalMoves:
                print("Nuke\nBoom!")
                ProgramBody()  # For the real game


def ProgramBody(): 


        global move_Counter , nuke 
        exit_test = int(input("\nplayer_Test_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nEnter 2 to Increment nuke.eta by one  \nEnter Option: "))
        if exit_test == 1:
            name = "Nuke"
            totalMoves = 5 
            currntPos = 0,0,0
            endPos = 500,0,500
            eta = 0
            owner = "Player_Test"
            angle = 1.9
            nuke = projectile(name,totalMoves,currntPos,endPos,eta,owner)
            nuke_list.append(nuke)
            launch_Nuke(nuke, currntPos, endPos, angle)
        elif exit_test == 2:
                print("List of nukes:")
                for nuke in nuke_list:
                    nuke.eta = nuke.eta + 1
                    nuke.display_Nuke()

        else:
            print("player_Test_Choice\nMove Was skipped") # Remove Later
            nuke.display_Nuke()
            move_Counter = move_Counter + 1    

ProgramBody()
