import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
width, height = 800, 600

# Create a new window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Number Drawing")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the numbers to be drawn
numbers = [
    [
        "1111",
        "1001",
        "1001",
        "1001",
        "1111"
    ],
    [
        "0110",
        "0010",
        "0010",
        "0010",
        "0111"
    ],
    [
        "1111",
        "0001",
        "1111",
        "1000",
        "1111"
    ],
    [
        "1111",
        "0001",
        "1111",
        "0001",
        "1111"
    ],
    [
        "1010",
        "1010",
        "1111",
        "0010",
        "1111"
    ],
    # Add more numbers here as needed
]

# Set the initial number index and size
number_index = 0
number_width = len(numbers[number_index][0])
number_height = len(numbers[number_index])
number_size = 50
number_x = (width - number_width * number_size) // 2
number_y = (height - number_height * number_size) // 2

# Main game loop
running = True
while running:
    # Clear the screen
    screen.fill(WHITE)

    # Draw the current number
    number = numbers[number_index]
    for y, row in enumerate(number):
        for x, pixel in enumerate(row):
            if pixel == '1':
                rect = pygame.Rect(number_x + x * number_size, number_y + y * number_size, number_size, number_size)
                pygame.draw.rect(screen, BLACK, rect)

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Increase the number index by one
                number_index = (number_index + 1) % len(numbers)

# Quit Pygame
pygame.quit()
