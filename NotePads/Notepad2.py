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
        print("Eta = %d" % (nuke.eta ))
        print("Pos = (%d,%d,%d)" % (nuke.currntPos))
        print("End Pos = (%d,%d,%d)" % (nuke.endPos))
        print("Owner = " + nuke.owner)
        print("\n")

nuke_list = []

def ProgramBody(): 
    global nuke 
    while True:
        choice = input("Enter 'a' to add a nuke, 'p' to print the list, or 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == 'a':
            name = "Nuke"
            totalMoves = 5 
            currntPos = 0,0,0
            EndPos = 500,0,500
            eta = 0
            owner = "playerone"
            nuke = projectile(name,totalMoves,currntPos,EndPos,eta,owner)
            nuke_list.append(nuke)
            print("Nuke added.")
        elif choice == 'p':
            print("List of nukes:")
            for nuke in nuke_list:
                nuke.eta = nuke.eta + 1
                nuke.display_Nuke()
        else:
            print("Invalid choice. Please try again.")

ProgramBody()
nuke.display_Nuke()