from engine import *


pygame.init()

#base window details
width = 1000
height = 1000
fullscreen = 0 # 0  for defined width and height, pygame.FULLSCREEN for fullscreen
title = "GameProject"

#window handling
window = Window(width, height, fullscreen, title)

# ground info
size = (100,100)
ground = Ground(window, Vector(width/2, height/2), Vector(0,0), size, "Green")

# player info
player = Player(window, Vector(100, 100), Vector(0,0), size, "Blue")
running = True
while running:

    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.velocity.x -= 1
            elif event.key == pygame.K_RIGHT:
                player.velocity.x += 1

        # if keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.velocity.x += 1

            elif event.key == pygame.K_RIGHT:
                player.velocity.x -= 1


    # object updating
    player.update()

    # object drawing
    window.clear()
    ground.draw()
    player.draw()

    window.swapBuffers()
pygame.quit()
