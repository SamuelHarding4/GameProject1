import pygame
from vector import *

class Window:
    def __init__(self, width,height, fullscreen, title):
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.title = title

        # makes the pygame window
        self.window = pygame.display.set_mode((width,height), fullscreen)

