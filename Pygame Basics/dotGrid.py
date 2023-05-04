import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
color = (255, 255, 255)

x = 25
y = 25
radius = 5

for row in range(19):
    for col in range(19):  
        pygame.draw.circle(screen, color, (x + col * 25, y + row * 25), radius)
    y += 25 
x += 25  
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
