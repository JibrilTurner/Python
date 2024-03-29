import pygame
import time
import random
pygame.init()


# Set up the display
display_width = 800
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
 
 # Define the snake properties
cubeSize = 20
snake_speed = 20
class parentSnake:
    def __init__(self, x, y, cubeSize, speed):
        self.x = x
        self.y = y
        self.cubeSize = cubeSize
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.length = 1
        self.body = [(x, y)]

    def handle_key_event(self, event):
        if event.key == pygame.K_w and self.dy != self.cubeSize:
            self.dx = 0
            self.dy = -self.cubeSize
        elif event.key == pygame.K_s and self.dy != -self.cubeSize:
            self.dx = 0
            self.dy = self.cubeSize
        elif event.key == pygame.K_a and self.dx != self.cubeSize:
            self.dx = -self.cubeSize
            self.dy = 0
        elif event.key == pygame.K_d and self.dx != -self.cubeSize:
            self.dx = self.cubeSize
            self.dy = 0
class parentFood:
    def __init__(self, x, y, cubeSize,amieaten):
        self.x = x
        self.y = y
        self.cubeSize = cubeSize
        self.amieaten = False

class parentTeleportFood: 
    def __init__(self, x1, y1, x2 ,y2, cubeSize,amieaten):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cubeSize = cubeSize
        self.amieaten = False

class lives:
    def __init__(self, lives, x, y):
        self.lives = lives
        self.cubeSize = cubeSize
        self.x = x
        self.y = y



def getNewCords():
    childFood.x = random.randint(0, (display_width - 400 -childFood.cubeSize) // cubeSize) * cubeSize
    childFood.y = random.randint(0, (display_height - 400 - childFood.cubeSize) // cubeSize) * cubeSize

def getNewCordsTeleport():
    #genrate random cords for teleport food
    childTeleportFood.x1 = random.randint(0, (display_width - 400 -childTeleportFood.cubeSize) // cubeSize) * cubeSize
    childTeleportFood.y1 = random.randint(0, (display_height - 400 - childTeleportFood.cubeSize) // cubeSize) * cubeSize
    childTeleportFood.x2 = random.randint(0, (display_width - 400 -childTeleportFood.cubeSize) // cubeSize) * cubeSize
    childTeleportFood.y2 = random.randint(0, (display_height - 400 - childTeleportFood.cubeSize) // cubeSize) * cubeSize

# Initialize lives
lives = 3

def resetGame():  # Decrements lives by one and resets snake
    global lives
    lives -= 1
    childSnake.x = display_width // 2
    childSnake.y = display_height // 2
    childSnake.dx = 0
    childSnake.dy = 0
    childSnake.length = 1
    childSnake.body = [(childSnake.x, childSnake.y)]
    time.sleep(.25)  # Pause for 1 second




# Define the clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)



# Initialize the snake
childSnake = parentSnake(display_width // 2, display_height // 2, cubeSize, snake_speed)
childFood = parentFood(200,200,cubeSize,False)
childTeleportFood = parentTeleportFood(200,200,400,400,cubeSize,False)



game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and childSnake.dy != childSnake.cubeSize:
                childSnake.dx = 0
                childSnake.dy = -childSnake.cubeSize
            elif event.key == pygame.K_s and childSnake.dy != -childSnake.cubeSize:
                childSnake.dx = 0
                childSnake.dy = childSnake.cubeSize
            elif event.key == pygame.K_a and childSnake.dx != childSnake.cubeSize:
                childSnake.dx = -childSnake.cubeSize
                childSnake.dy = 0
            elif event.key == pygame.K_d and childSnake.dx != -childSnake.cubeSize:
                childSnake.dx = childSnake.cubeSize
                childSnake.dy = 0

    # Update snake's position
    childSnake.x += childSnake.dx
    childSnake.y += childSnake.dy

    # Update the snake's body
    childSnake.body.append((childSnake.x, childSnake.y))  # Add the new head segment

    # If the snake ate food, don't remove the tail segment
    if len(childSnake.body) > childSnake.length:
        del childSnake.body[0]  
    # Remove the tail segment

    # Clear the screen
    display.fill(black)

    # Draw the snake
 
    for segment in childSnake.body:
        pygame.draw.rect(display, white, [segment[0], segment[1], childSnake.cubeSize, childSnake.cubeSize])

    # Draw the childFood
  
    # if snake gits the wall game over
    if childSnake.x >= display_width  or childSnake.x < 0 or childSnake.y >= display_height  or childSnake.y < 0:
        resetGame()
    else:
        pass                
        
    # check snake collison 
    for segment in childSnake.body[:-1]: 
        if segment == childSnake.body[-1]:
            resetGame()

    # check collision with parentTeleportFood
    if childSnake.x == childTeleportFood.x1 and childSnake.y == childTeleportFood.y1:
        childTeleportFood.amieaten = True
        getNewCordsTeleport()
    if childSnake.x == childTeleportFood.x2 and childSnake.y == childTeleportFood.y2:
        childTeleportFood.amieaten = True
        getNewCordsTeleport()
    # Check collision with parentFood
    if childSnake.x == childFood.x and childSnake.y == childFood.y:
        childSnake.length += 1  # Increment the length by one
        getNewCords()  # Generate new coordinates for the parentFood
        
    # display score 
    font = pygame.font.SysFont("ariral", 72)
    text = font.render(str(childSnake.length), True, white)
    display.blit(text, (0, 0))

        
    # Draw the parentFood if not eaten
    if not childFood.amieaten:
        pygame.draw.rect(display, white, [childFood.x, childFood.y, childFood.cubeSize, childFood.cubeSize])

    # initialize live cubes on upper left corner remove one life(cube) snake dies
    if lives == 3:
        pygame.draw.rect(display, white, [740, 0, childSnake.cubeSize, childSnake.cubeSize])
        pygame.draw.rect(display, white, [710, 0, childSnake.cubeSize, childSnake.cubeSize])
        pygame.draw.rect(display, white, [680, 0, childSnake.cubeSize, childSnake.cubeSize])
    if lives == 2:
        pygame.draw.rect(display, white, [710, 0, childSnake.cubeSize, childSnake.cubeSize])
        pygame.draw.rect(display, white, [680, 0, childSnake.cubeSize, childSnake.cubeSize])
    if lives == 1:
        pygame.draw.rect(display, white, [680, 0, childSnake.cubeSize, childSnake.cubeSize])


    # draw the parentTeleportFood if not eaten
    if not childTeleportFood.amieaten:
        pygame.draw.rect(display, 'red', [childTeleportFood.x1, childTeleportFood.y1, childTeleportFood.cubeSize, childTeleportFood.cubeSize])
        pygame.draw.rect(display, 'blue', [childTeleportFood.x2, childTeleportFood.y2, childTeleportFood.cubeSize, childTeleportFood.cubeSize])
    
    # check if life equals 0 if so game over
    if lives == 0:
        game_over = True    

    # If parentFood is eaten, generate new coordinates and draw the parentFood
    if childFood.amieaten:
        getNewCords()
        x = 1 
        x = x + 1
        pygame.draw.rect(display, white, [segment[0], segment[x], childSnake.cubeSize, childSnake.cubeSize])
        childFood.amieaten = False



    # If parentTeleportFood is eaten, telport snake to other parentTeleportFood work with both cubes
    if childTeleportFood.amieaten:
        childSnake.x = childTeleportFood.x2
        childSnake.y = childTeleportFood.y2
        childTeleportFood.amieaten = False
    
    # if parentTeleportFood is eaten, generate new coordinates and draw the parentTeleportFood
    if childTeleportFood.amieaten == True:
        x = 1 
        x = x + 1
        pygame.draw.rect(display, 'red', [segment[0], segment[x], childSnake.cubeSize, childSnake.cubeSize])
        getNewCords()
        childTeleportFood.amieaten = False


    
    

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(childSnake.speed)

# Quit the game
pygame.quit()