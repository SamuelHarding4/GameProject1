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
groundSize = (1000,10)
ground = Ground(window, Vector(0, height - groundSize[1]), Vector(0,0), groundSize, "Green")

# player info
playerSize = (50,50)
player = Player(window, Vector(100, height - 100), Vector(0,0), playerSize, "Blue")

running = True
# main run loop
while running:

    # input handling
    for event in pygame.event.get():
        # if quit
        if event.type == pygame.QUIT:
            running = False

        # if keydown
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft = True
            elif event.key == pygame.K_RIGHT:
                player.moveRight = True

            elif event.key == pygame.K_SPACE:
                player.doJump = True

            else:
                pass

        # if keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moveLeft = False

            elif event.key == pygame.K_RIGHT:
                player.moveRight = False

            elif event.key == pygame.K_SPACE:
                player.doJump = False

            else:
                pass


    # object updating
    dt = window.getDt()
    player.update(dt)

    # object logic
    if player.hit(ground) == "top":
        player.pos.y = ground.pos.y - player.height

    # object drawing
    window.clear()
    ground.draw()
    player.draw()

    window.swapBuffers()
pygame.quit()
