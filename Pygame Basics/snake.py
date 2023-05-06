import pygame
import time
import random
pygame.init()

# Set up the display
display_width = 800
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
 
class Snake:
    def __init__(self, x, y, cubeSize, speed):
        self.x = x
        self.y = y
        self.cubeSize = cubeSize
        self.speed = speed
        self.x_change = 0
        self.y_change = 0
        self.length = 1  # Initialize the length as 1
        self.body = [(x, y)]  # Initialize with a single segment

class food:
    def __init__(self, x, y, cubeSize,amieaten):
        self.x = x
        self.y = y
        self.cubeSize = cubeSize
        self.amieaten = False


# Snake properties
cubeSize = 20
snake_speed = 15

# 
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Initialize the snake
snake_obj = Snake(display_width // 2, display_height // 2, cubeSize, snake_speed)
food_obj = food(200,200,cubeSize,False)

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake_obj.y_change != snake_obj.cubeSize:
                snake_obj.x_change = 0
                snake_obj.y_change = -snake_obj.cubeSize
            elif event.key == pygame.K_s and snake_obj.y_change != -snake_obj.cubeSize:
                snake_obj.x_change = 0
                snake_obj.y_change = snake_obj.cubeSize
            elif event.key == pygame.K_a and snake_obj.x_change != snake_obj.cubeSize:
                snake_obj.x_change = -snake_obj.cubeSize
                snake_obj.y_change = 0
            elif event.key == pygame.K_d and snake_obj.x_change != -snake_obj.cubeSize:
                snake_obj.x_change = snake_obj.cubeSize
                snake_obj.y_change = 0

    # Update snake's position
    snake_obj.x += snake_obj.x_change
    snake_obj.y += snake_obj.y_change

    # Update the snake's body
    snake_obj.body.append((snake_obj.x, snake_obj.y))  # Add the new head segment

    if len(snake_obj.body) > snake_obj.length:
        del snake_obj.body[0]  # Remove the tail segment
    # Clear the screen
    display.fill(black)

    # Draw the snake
    for segment in snake_obj.body:
        pygame.draw.rect(display, white, [segment[0], segment[1], snake_obj.cubeSize, snake_obj.cubeSize])
    
    def getNewCords():
        food_obj.x = random.randint(0, (display_width - food_obj.cubeSize) // 20) * 20
        food_obj.y = random.randint(0, (display_height - food_obj.cubeSize) // 20) * 20

    # Check collision with food
    if snake_obj.x == food_obj.x and snake_obj.y == food_obj.y:
        snake_obj.length += 1  # Increment the length by one
        getNewCords()  # Generate new coordinates for the food

        
    # Draw the food if not eaten
    if not food_obj.amieaten:
        pygame.draw.rect(display, white, [food_obj.x, food_obj.y, food_obj.cubeSize, food_obj.cubeSize])

    # If food is eaten, generate new coordinates and draw the food
    if food_obj.amieaten:
        getNewCords()
        x = 1 
        x = x + 1
        pygame.draw.rect(display, white, [segment[0], segment[x], snake_obj.cubeSize, snake_obj.cubeSize])
        food_obj.amieaten = False

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(snake_obj.speed)

# Quit the game
pygame.quit()
