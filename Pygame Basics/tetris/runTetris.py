import pygame

cubeSize = 20
cubeSpeed = 20  

class Block:
    def __init__(self, points, color,cubeSize,cubeSpeed):
        self.points = points
        self.color = color
        self.cubeSize = cubeSize
        self.cubeSpeed = cubeSpeed

    @staticmethod
    def create_long_block():
        points = [(0, 0), (0, 1), (0, 2), (0, 3)]
        color = (0, 255, 0)
        return Block(points, color)

    @staticmethod
    def create_square_block():
        points = [(0, 0), (0, 1), (1, 0), (1, 1)]
        color = (0, 0, 255)
        return Block(points, color)

    @staticmethod
    def create_l_block():
        points = [(0, 0), (0, 1), (0, 2), (1, 2)]
        color = (255, 0, 0)
        return Block(points, color)
    


def draw_block_to_display(x, y, block):
    for point in block.points:
        pygame.draw.rect(screen, block.color, (x + point[0] * 25, y + point[1] * 25, 25, 25))

def draw_grid_to_display(x, y):
    for row in range(19):
        for col in range(19):  
            pygame.draw.rect(screen, color, (x + col * 25, y + row * 25, 25, 25))
        y += 25 
    x += 25  
    pygame.display.update()

def control_block(block):
    input = pygame.key.get_pressed()
    if input[pygame.K_d]:
    
        block.move_right()
    if input[pygame.K_a]:
        block.move_left()

    return block


pygame.init()

screen = pygame.display.set_mode((500, 500))
color = (255, 255, 255)

block = Block.create_long_block()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    
            # Check for key presses

        
    block = control_block(block)
    screen.fill(color)
    draw_block_to_display(25, 25, block)
    pygame.display.update()
