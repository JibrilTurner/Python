def do_something():
    exit_test = int(input("enter 0 to exit Or enter 1 Make a move: "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output


class projectile:
  def __init__(self, name,deltaX,deltaY,totalMoves, maxYpos ,maxXpos,numberOfProjectile,radius,startingXpos,startingYpos ):
    self.totalMoves = totalMoves 
    self.maxYpos = maxYpos
    self.maxXpos = maxXpos
    self.currentPos = maxXpos,maxYpos
    self.numberOfProjectile = numberOfProjectile 
    self.radius = radius 
    self.startingXpos = startingXpos
    self.startingYpos = startingYpos
    self.deltaX = deltaX
    self.deltaY = deltaY
    self.name = name 

p2 = PlayerStats("Jibril","mage",17.5,10)
Nuke = projectile("Nuke",)




counter = 0 
do = True
while do == True:
    if do_something() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break;        
    else: 
        do == True
        counter = counter + 1 
        if counter > 5: 
            print("boom")
            else:
                
        print(counter)
        #Write Code Here
        print("\nNot Exiting\n")
        
