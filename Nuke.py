def do_something():
    exit_test = int(input("Magic enter 0 to exit Or enter 1 to loop: "))
    if exit_test == 1:
        alt = 1
        print(alt)
        return alt
    else:
        alt = 0
        return alt
    



class projectile:
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 


def LanchNuke():
    nuke = projectile("Nuke",5,(0,0),1)
    nuke.totalMoves = -1 
    do = True
    while do == True:
    
        if do_something() == 0:
            #Instead of Breaking Send to Another Function Or Break To Close program
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
                    #Write Code Here
                    print("\nNot Exiting\n")

do_something()
