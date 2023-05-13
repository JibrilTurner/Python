import MyFile

def menu():
    Exit = False
    while not Exit:
        print("Press 0 to exit")
        print("1. 1tartGame")
        
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            Exit = True
        elif choice == 1:
            print("Starting Game...")
            runTetris()
       
        else:
            print("Invalid choice")
