import snake
import pygame
import random
import time
    
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

white = (255, 255, 255)
black = (0, 0, 0)