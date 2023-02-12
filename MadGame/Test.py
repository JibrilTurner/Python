"""
Basic "Hello, World!" program in Pygame

This program is designed to demonstrate the basic capabilities
of Pygame. It will:
- Create a game window
- Fill the background with white
- Draw some basic shapes in different colors
- Draw some text in a specified size and color
- Allow you to close the window
"""

# Import and initialize the pygame library
import pygame

pygame.init()


# Set the width and height of the output window, in pixels
WIDTH = 1920
HEIGHT = 1030

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
screen.fill((255, 255, 255))
x = 500
if x == 4:
    print("Why")
else:
    for x in range(5):
        print(x)
        x = x + 1
    print("Whdy")

red_square = pygame.Rect((90, x), (100, 100))
pygame.draw.rect(screen, (200, 50, 0), red_square, 1)

red_square = pygame.Rect((250, x), (100, 100))
pygame.draw.rect(screen, (200, 50, 0), red_square, 1)

red_square = pygame.Rect((410, x), (100, 100))
pygame.draw.rect(screen, (200, 200, 0), red_square, 1)


# Draw a blue circle with a radius of 50 in the center of the screen

pygame.display.update()
pygame.quit()

