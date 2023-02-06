def do_something():
    exit_test = int(input("enter 0 to exit Or enter 1 to loop: "))
    if exit_test == 1:
        test_output = True
    else:
        test_output = False
    return test_output
    
do = True
while do == True:
    if do_something() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break;        
    else: 
        do == True
        #Write Code Here
        print("\nNot Exiting\n")
<<<<<<< HEAD
=======
        
        
>>>>>>> 7d77e12677379fda1f93344f59f6c6c45278e690
