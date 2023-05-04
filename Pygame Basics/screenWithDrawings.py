import pygame, sys

pygame.init()                                                   
screen = pygame.display.set_mode((500,500))                      
clock = pygame.time.Clock()
testSurface = pygame.Surface((200,200))

while True:                                                      
    for event in pygame.event.get():                             
        if event.type == pygame.QUIT:                            
            pygame.quit()                                        
            sys.exit       
    screen.fill((175,215,70))    
    screen.blit(testSurface,(250,250))                       
    pygame.display.update()                                      
    clock.tick(60)
