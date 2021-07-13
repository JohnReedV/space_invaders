import pygame
import random
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders >:)")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
lost = pygame.image.load("youlose.png")
background = pygame.image.load("back.gif")

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
stextx = 340
stexty = 10

playerimg = pygame.image.load("player.png")
playerx = 370
playery = 530
playerxchange = 0

enemy1img = []
enemy1x = []
enemy1y = []
enemy1xchange = []
enemy1ychange = []
enemyamount = 6

for i in range(enemyamount):
    enemy1img.append(pygame.image.load("enemy1.png"))
    enemy1x.append(random.randrange(65, 736))
    enemy1y.append(20)
    enemy1xchange.append(.25)
    enemy1ychange.append(.01)

missileimg = pygame.image.load("missile.png")
missilex = 0
missiley = 480
missilexchange = 0
missileychange = .4
bullet_sate = "ready"

def scoref(x, y):
    score1 = font.render("Score : " + str(score), True, (0, 0, 0))
    screen.blit(score1, (x, y))

def player(x,y):
    screen.blit(playerimg,(x, y))

def enemy1(x,y, i):
    screen.blit(enemy1img[i],(x, y))

def missile(x,y):
    global bullet_sate
    screen.blit(missileimg,(x + 16, y + 10))
    bullet_sate = "fire"

def iscollision(enemyx, enemyy, missilex, missiley):
    distance = math.sqrt(math.pow(enemyx - missilex,2) + math.pow(enemyy - missiley,2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerxchange = -0.2
            if event.key == pygame.K_LEFT:
                playerxchange = -0.2
            if event.key == pygame.K_d:
                playerxchange = +0.2
            if event.key == pygame.K_RIGHT:
                playerxchange = +0.2
            if event.key == pygame.K_SPACE:
                if bullet_sate == "ready":
                    missilex = playerx
                    missile(playerx, missiley)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerxchange = 0

    playerx += playerxchange

    if playerx < 0:
        playerx = 0
    elif playerx > 736:
        playerx = 736

    for i in range(enemyamount):
        enemy1(enemy1x[i], enemy1y[i], i)
        enemy1y[i] += .01
        enemy1x[i] += enemy1xchange[i]
        if enemy1x[i] <= 0:
            enemy1xchange[i] = .25
            enemy1x[i] += enemy1xchange[i]
        elif enemy1x[i] >= 736:
            enemy1xchange[i] = -.25
            enemy1y[i] += enemy1ychange[i]

        collision = iscollision(enemy1x[i], enemy1y[i], missilex, missiley)

        if collision:
            missiley = 480
            bullet_sate = "ready"
            score = score + 1
            enemy1x[i] = random.randint(0, 736)
            enemy1y[i] = random.randint(10, 30)

        if enemy1y[i] >= 500:
            screen.blit(lost, (220, 100))
            pygame.display.update()
            time.sleep(3)
            break

    if bullet_sate == "fire":
        missile(missilex, missiley)
        missiley -= missileychange

    if missiley <= 0:
        missiley = 480
        bullet_sate = "ready"

    player(playerx, playery)
    scoref(stextx, stexty)
    pygame.display.update()