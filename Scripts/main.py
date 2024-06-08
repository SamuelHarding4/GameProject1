from engine import *


pygame.init()

#base window details
width = 1000
height = 1000
fullscreen = 0 # 0  for defined width and height, pygame.FULLSCREEN for fullscreen
title = "GameProject"

#window handling
window = Window(width, height, fullscreen, title)

# ground information
size = (100,100)
ground = Ground(window, Vector(width/2, height/2), Vector(0,0), size, "Green")

running = True
while running:

    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # object updating

    # object drawing
    window.clear()
    ground.draw()


    window.swapBuffers()
pygame.quit()
