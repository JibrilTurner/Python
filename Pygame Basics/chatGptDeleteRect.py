import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the display surface
display_width = 800
display_height = 600

# Create the display surface
display_surface = pygame.display.set_mode((display_width, display_height))

# Set the background color
background_color = (0, 0, 0)  # Black

# Set the rectangle properties
rectangle_color = (255, 0, 0)  # Red
rectangle_rect = pygame.Rect(100, 100, 200, 150)  # x, y, width, height

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
    keys = pygame.key.get_pressed()

    # Check if the "D" key is pressed
    if keys[pygame.K_d]:
        draw_rectangle = False
    if keys[pygame.K_a]:
        draw_rectangle = True
    # Clear the display surface with the background color
    display_surface.fill(background_color)

    # Draw the rectangle if the flag is set to True
    if draw_rectangle:
        pygame.draw.rect(display_surface, rectangle_color, rectangle_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
