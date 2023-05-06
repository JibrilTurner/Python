# import pygame module in this program
import pygame

def draw_rect_alpha(surface, color, rect): # inputs to function 
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) 
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def transparent_rect(surface, color, rect, alpha): # inputs to function 
	shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) 
	pygame.draw.rect(shape_surf, color + (alpha,), shape_surf.get_rect())
	surface.blit(shape_surf, rect)
	
pygame.init()

green = (88,232,124)
purple = (188,147,250)
white = (255, 255, 255)
blue = (50,135,234,255)
magenta = (0, 0, 0)
red = (214, 50, 72)
yellow = (241,242,94)

X = 600
Y = 800
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Drawing')
display_surface.fill(white)

# define the colors and coordinates for each rectangle
rect_data = [
    [(88, 239, 124), (0, 0, 300, 400)],
    [(241,242,94), (300, 0, 600, 400)],
    [(0, 0, 255), (0, 400, 300, 800)],
    [(255, 0, 0), (300, 400, 600, 800)],
]

# draw each rectangle using a for loop
for color, coords in rect_data:
    pygame.draw.rect(display_surface, color, coords)


draw_rect_alpha(display_surface, (255, 255, 255, 50), (50, 50, 500, 650))  # number inidicates transparancy 
draw_rect_alpha(display_surface, (255, 255, 255, 50), (150, 150, 300, 450))  # number inidicates transparancy

while True :	
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			pygame.quit()
			quit()
		pygame.display.update()
