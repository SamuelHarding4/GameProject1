import pygame
from vector import *

class Window:
    def __init__(self, width : int, height : int, fullscreen , title : str):
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.title = title

        # makes the pygame window
        self.window = pygame.display.set_mode((width,height), fullscreen)
        pygame.display.set_caption(title)

    def swapBuffers(self):
        pygame.display.flip()

    def clear(self):
        # pygame window referenced
        self.window.fill("Red")
