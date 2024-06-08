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
        self.window.fill("DarkGreen")

class Ground:
    def __init__(self, window, pos, velocity, size, color):
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity
        self.width,self.height = size
        self.color = color

    def draw(self):
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))
