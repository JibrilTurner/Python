import pygame, sys

pygame.init()                                                    # starts everything such as sound grapfics ect 
screen = pygame.display.set_mode((400,500))                      # makes the windows x,y 

while True:                                                      # keeps the display open until something insddes closes it  
    for event in pygame.event.get():                             # Checking for every event
        if event.type == pygame.QUIT:                            # If the event of quiting is occuring then,
            pygame.quit()                                        # quits pygame 
            sys.exit                                             # really kills the program
    pygame.display.update()                                      # this functin will display whatever on the window 

