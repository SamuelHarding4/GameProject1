import pygame
from vector import *
import time

class Window:
    def __init__(self, width : int, height : int, fullscreen , title : str):
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.title = title
        self.previousTime = time.time()


        # makes the pygame window
        self.window = pygame.display.set_mode((width,height), fullscreen)
        pygame.display.set_caption(title)

    def swapBuffers(self):
        pygame.display.flip()

    def clear(self):
        # pygame window referenced
        self.window.fill("DarkGreen")

    def getDt(self):
        currentTime = time.time()
        dt = currentTime - self.previousTime
        self.previousTime = currentTime
        return dt

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

class Player:
    def __init__(self, window, pos, velocity, size, color):
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity # Vector(100,100)
        self.width,self.height = size
        self.color = color
        self.gravity = Vector(0,9.8)
        self.moveLeft = False
        self.moveRight = False
        self.moveDown = False
        self.moveUp = False

    def update(self, dt):
        if self.moveLeft == True:
            self.velocity.x -= 100

        if self.moveRight == True:
            self.velocity.x += 100

        if self.moveUp == True:
            self.velocity.y -= 100

        if self.moveDown == True:
            self.velocity.y += 100
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.pos += self.velocity * dt

    def draw(self):
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def hit(self, object):
        # check if any sides are inside each other
        if ((self.pos.x > object.pos.x and self.pos.x < object.pos.x + self.width) or \
            (self.pos.x + self.width > object.pos.x and self.pos.x + self.width < object.pos.x + object.width)) and \
                ((self.pos.y > object.pos.y and self.pos.y < object.pos.y + self.height) or \
            (self.pos.y + self.height > object.pos.y and self.pos.y + self.height < object.pos.y + object.height)):
            return True
        return False
