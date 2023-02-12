def do_something():
    exit_test = int(input("enter 0 to exit Or enter 1 Make a move: "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output






counter = 0 
do = True
while do == True:
    if do_something() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break;        
    else: 
        do == True
        if counter == 5: 
            print("boom")
        else:




            counter = counter + 1 
            print(counter)
        #Write Code Here
        print("\nNot Exiting\n")
        
