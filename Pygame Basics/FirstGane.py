import pygame
import time 
# Initialize Pygame
pygame.init()

# Set the dimensions of the display surface
display_width = 800
display_height = 600
x = 50
y = 0
speed = 2  # Adjust the speed of movement

# Create the display surface
display_surface = pygame.display.set_mode((display_width, display_height))

# Set the background color
background_color = (0, 0, 0)  # Black

# Set the rectangle properties
rectangle_color = (255, 0, 0)  # Red
border_color = (255, 255, 255)  # White
rectangle_rect = pygame.Rect(x, y, 50,50)  # x, y, width, height

gravity = 0.5 # Adjust the gravity 

# Flag to determine if the rectangle should be drawn or deleted
draw_rectangle = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys









    # future control funtion 
    keys = pygame.key.get_pressed()

    # Move the rectangle up if the "W" key is pressed and within the border
    if keys[pygame.K_w] and y > 0:
        y -= speed

    # Move the rectangle down if the "S" key is pressed and within the border
    if keys[pygame.K_s] and y + rectangle_rect.height < display_height:
        y += speed

    # Move the rectangle right if the "D" key is pressed and within the border
    if keys[pygame.K_d] and x + rectangle_rect.width < display_width:
        x += speed

    # Move the rectangle left if the "A" key is pressed and within the border
    if keys[pygame.K_a] and x > 0:
        x -= speed
            
    if keys[pygame.K_SPACE]:
            for _ in range(15):
                y += speed
                time.sleep(0.1)





 
    # game physics 
    if  y + rectangle_rect.height < display_height:
        y += gravity

    




    # Clear the display surface with the background color
    display_surface.fill(background_color)

    # Draw the border rectangle
    border_rect = pygame.Rect(0, 0, display_width, display_height)
    pygame.draw.rect(display_surface, border_color, border_rect, 2)



    # Draw the inner rectangle
    pygame.draw.rect(display_surface, rectangle_color, rectangle_rect)

    # Update the rectangle's position
    rectangle_rect.y = y  # Adjust the gravity
    rectangle_rect.x = x

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
