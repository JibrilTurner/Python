# import pygame module in this program
import pygame


pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (240,248,255)
black = (0, 0, 0)
red = (255, 0, 0)

X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Drawing')
display_surface.fill(white)

pygame.draw.polygon(display_surface, blue,[(146, 0), (291, 106),(236, 277), (56, 277), (0, 106)],0) # p1(x,y) p2(x,y) p3(x,y) p4(x,y) p5(x,y) hollow(1 OR 0)
pygame.draw.line(display_surface, green,(60, 300), (120, 300), 1)								 	# Start(x,y) End(x,y) Thickness(x) hollow(1 OR 0)
pygame.draw.circle(display_surface,green, (300, 50), 5, 0)											# Pos(x,y) Raduis(x) hollow(1 OR 0)			
pygame.draw.ellipse(display_surface, black,(300, 250, 40, 90), 1)									# Diminsions (x,y,z,j) hollow(1 OR 0)
pygame.draw.rect(display_surface, black,(150, 300, 100, 50),0)										# Diminsions (x,y,z,j) hollow(1 OR 0)

while True :	
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()
			quit()
		pygame.display.update()
