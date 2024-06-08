import pygame
from vector import *
import time


class Window:
    def __init__(self, width: int, height: int, fullscreen, title: str):
        """
        Constructor for a window

        :param width: width of window
        :param height: height of window
        :param fullscreen: fullscreen mode decision
        :param title: title of window
        """
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.title = title
        self.previousTime = time.time()

        # makes the pygame window with defined window sizes
        self.window = pygame.display.set_mode((width,height), fullscreen)
        pygame.display.set_caption(title)

    def swapBuffers(self):
        """
        Swaps buffered surface to visible surface

        """
        pygame.display.flip()

    def clear(self):
        """
        clears the frame of the window

        """
        # pygame window referenced
        self.window.fill("LightBlue")

    def getDt(self):
        """
        works out the delta time of the computer

        :return: the delta time of the computer
        """
        currentTime = time.time()
        dt = currentTime - self.previousTime
        self.previousTime = currentTime
        return dt


class Ground:
    def __init__(self, window: "Window", pos: "Vector", velocity: "Vector", size: (int, int), color: str):
        """
        class for ground obstacle

        :param window: which window to draw it to
        :param pos: position of the ground on the window
        :param velocity: velocity of the ground
        :param size: size of the ground
        :param color: color of the ground
        """
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity
        self.width,self.height = size #decomposes (100,100) into different variables
        self.color = color

    def draw(self):
        """
        draws a rectangle with the ground obstacle properties
        """
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))


class Player:
    def __init__(self, window, pos, velocity, size, color):
        """
        class for player object

        :param window: which window to draw it to
        :param pos: position of the player on the window
        :param velocity: velocity of the player
        :param size: size of the player
        :param color: color of the player
        """
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity # Vector(100,100)
        self.width,self.height = size
        self.color = color
        self.gravity = Vector(0,1.5)
        self.onGround = False

        # used for continued movement when button pressed once
        self.moveLeft = False
        self.moveRight = False
        self.doJump = False

    def update(self, dt):
        """
        updates player pos and velocity based on key presses and gravity

        :param dt: delta time of the window
        """

        if self.moveLeft:
            self.velocity.x -= 100

        if self.moveRight:
            self.velocity.x += 100

        if self.doJump:
            self.jump()

        self.velocity += self.gravity  # adds gravity to velocity
        self.velocity.x *= 0.9  # slows down the velocity if the button is not pressed
        self.pos += self.velocity * dt  # adds velocity to the position

    def draw(self):
        """
        draws the player

        """
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def hit(self, obstacle):
        """
        determines if player has hit the obstacle, and returns what side of the obstacle it has hit

        :param obstacle: obstacle to be collision checked
        :return: side hit of the obstacle
        """
        # Determine the sides of self
        self_left = self.pos.x
        self_right = self.pos.x + self.width
        self_top = self.pos.y
        self_bottom = self.pos.y + self.height

        # Determine the sides of obstacle
        obj_left = obstacle.pos.x
        obj_right = obstacle.pos.x + obstacle.width
        obj_top = obstacle.pos.y
        obj_bottom = obstacle.pos.y + obstacle.height

        # Check for collision
        if self_right > obj_left and self_left < obj_right and self_bottom > obj_top and self_top < obj_bottom:
            # Determine the side of the collision
            if self_bottom > obj_top > self_top:
                self.onGround = True
                return "top"
            elif self_top < obj_bottom < self_bottom:
                return "bottom"
            elif self_right > obj_left > self_left:
                return "left"
            elif self_left < obj_right < self_right:
                return "right"
        return False

    def jump(self):
        if self.onGround:
            self.velocity.y = -700
            self.onGround = False
