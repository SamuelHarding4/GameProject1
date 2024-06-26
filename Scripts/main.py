from engine import *


pygame.init()

#base window details
useScreen = False # change to use fullscreen
width = 2000
height = 1000
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
title = "GameProject"

#window handling
window = Window(width, height, 0, title)
if useScreen:
    window = Window(screenWidth, screenHeight, pygame.FULLSCREEN, "Practice project")
    width = screenWidth
    height = screenHeight


# ground info
groundSize = (width,10)
ground = Ground(window, Vector(0, height - groundSize[1]), Vector(0,0), groundSize, "Green")

# player info
playerSize = (50,50)
player = Player(window, Vector(100, height - 100), Vector(0,0), playerSize, "Blue")

# ladder info
ladderSize = (100,200)
ladder = Ladder(window, Vector(200, height - 300), Vector(0,0), ladderSize, "Yellow")

# turrent info
turretSize = (100,100)
turret = Turret(window, Vector(width - 300, height - 300), Vector(0,0), turretSize, "Black")

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

            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_LEFT:
                player.moveLeft = True
            elif event.key == pygame.K_RIGHT:
                player.moveRight = True

            elif event.key == pygame.K_SPACE:
                player.doJump = True

            elif event.key == pygame.K_DOWN:
                player.moveDown = True

            elif event.key == pygame.K_UP:
                player.moveUp = True

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

            elif event.key == pygame.K_DOWN:
                player.moveDown = False

            elif event.key == pygame.K_UP:
                player.moveUp = False

            else:
                pass


    # object updating
    dt = window.getDt()
    player.update(dt)

    # object logic
    turret.shoot()
    for bullet in turret.bullets:
        bullet.update(dt)
        if bullet.pos.x < 0:
            turret.bullets.remove(bullet)

        if player.hit(bullet):
            player.moveLeft = False
            player.moveRight = False
            turret.bullets.remove(bullet)
            player.velocity += Vector(bullet.velocity.x * 10, -200)

    if player.hit(ground):
        player.pos.y = ground.pos.y - player.height
        player.velocity = Vector(0,0)

    if player.hit(ladder):
        pass

    # object drawing
    window.clear()
    ground.draw()
    ladder.draw()
    turret.draw()
    for bullet in turret.bullets:
        bullet.draw()
    player.draw()
    window.swapBuffers()
pygame.quit()
