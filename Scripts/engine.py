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
        self.forceGravity = True
        self.onGround = False
        self.onLadder = False

        # used for continued movement when button pressed once
        self.speed = 500
        self.moveLeft = False
        self.moveRight = False
        self.doJump = False
        self.moveUp = False
        self.moveDown = False

    def update(self, dt):
        """
        updates player pos and velocity based on key presses and gravity

        :param dt: delta time of the window
        """

        if self.moveLeft:
            self.velocity.x = -self.speed

        if self.moveRight:
            self.velocity.x = self.speed

        if self.doJump:
            self.jump()

        if self.onLadder:
            self.forceGravity = False
            if self.moveDown:
                self.velocity.y = self.speed

            if self.moveUp:
                self.velocity.y = -self.speed
            else:
                pass
        else:
            self.forceGravity = True

        if self.forceGravity:
            self.velocity += self.gravity  # adds gravity to velocity
        self.velocity.x = self.velocity.x * 0.95  # slows down the velocity if the button is not pressed
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

            # check if on ladder or ground
            if isinstance(obstacle, Ladder):
                self.onLadder = True
                self.velocity = Vector(0,0)

            if isinstance(obstacle, Ground):
                self.onGround = True

            # Determine the side of the collision
            if self_bottom > obj_top > self_top:
                return "top"
            elif self_top < obj_bottom < self_bottom:
                return "bottom"
            elif self_right > obj_left > self_left:
                return "left"
            elif self_left < obj_right < self_right:
                return "right"
            else:
                pass
        else:
            self.onLadder = False
        return False

    def jump(self):
        if self.onGround or self.onLadder:
            self.velocity.y = -700
            self.onGround = False

class Ladder:
    def __init__(self, window: "Window", pos: "Vector", velocity: "Vector", size: (int, int), color: str):
        """
        class for ladder obstacle

        :param window: which window to draw it to
        :param pos: position of the ladder on the window
        :param velocity: velocity of the ladder
        :param size: size of the ladder
        :param color: color of the ladder
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
        draws a rectangle with the ladder obstacle properties
        """
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))


class Turret:
    def __init__(self, window: "Window", pos: "Vector", velocity: "Vector", size: (int, int), color: str):
        """
        class for ground obstacle

        :param window: which window to draw it to
        :param pos: position of the turret on the window
        :param velocity: velocity of the turret
        :param size: size of the turret
        :param color: color of the turret
        """
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity
        self.width,self.height = size # decomposes (100,100) into different variables
        self.color = color
        self.bullets = []
        self.lastTime = time.time()

    def draw(self):
        """
        draws a rectangle with the ground obstacle properties
        """
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def shoot(self):
        if time.time() - self.lastTime > 2:
            bulletSize = (20,20)
            bullet = turretBullet(self.window, Vector(self.pos.x, self.pos.y + self.height / 2), Vector(-100,0), bulletSize, "White")
            self.bullets.append(bullet)
            self.lastTime = time.time()


class turretBullet:
    def __init__(self, window: "Window", pos: "Vector", velocity: "Vector", size: (int, int), color: str):
        """
        class for bullet obstacle

        :param window: which window to draw it to
        :param pos: position of the bullet on the window
        :param velocity: velocity of the bullet
        :param size: size of the bullet
        :param color: color of the bullet
        """
        # window object
        self.window = window
        # windowSurface actually the drawable canvas
        self.windowSurface = window.window
        self.pos = pos # Vector(100,100)
        self.velocity = velocity
        self.width,self.height = size # decomposes (100,100) into different variables
        self.color = color

    def draw(self):
        """
        draws a rectangle with the bullet obstacle properties
        """
        pygame.draw.rect(self.windowSurface, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def update(self,dt):
        self.pos += self.velocity * dt  # adds velocity to the position
