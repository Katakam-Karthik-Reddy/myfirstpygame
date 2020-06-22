import pygame
import random
import math

# intiatize the pygame
pygame.init()

# speed of the player
score_value = 0
player_speed = 10
enemyX_speed = 2
enemyY_speed = 30
# creating the game windows
screen = pygame.display.set_mode((800, 600))

# title
pygame.display.set_caption('aliens')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# background of the game
background = pygame.image.load('background.jpg')

# player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 4
for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(enemyX_speed)
    enemyY_change.append(enemyY_speed)


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def bullet(x, y):
    screen.blit(bulletimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))


# creating a function to cheak the collision is happend or not
distance = 0


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                         (math.pow(enemyY-bulletY, 2)))
    if distance <= 27:
        return True
    else:
        return False


# distance1 = 0


# def iscollision1(playerX, playerY, enemyX, enemyY):
#     distance1 = math.sqrt((math.pow(playerX-enemyX, 2)) +
#                           (math.pow(playerY-enemyY, 2)))
#     if distance1 <= 27:
#         return True
#     else:
#         return False

# Displaying the score
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


    # creating a quit feature//game loop
    # This is ensures that until we click quitbutton windows will not close
running = True
while running:
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = player_speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -player_speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # copying the position of the player at the time we press the spacebar
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w:
                playerX_change = 0
                playerY_change = 0
    playerX += playerX_change
    playerY += playerY_change

    # player boundery
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # enemy movement
    for i in range(no_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = enemyX_speed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -enemyX_speed
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = (random.randint(0, 735))
            enemyY[i] = (random.randint(0, 50))
        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # # game end
    # end = iscollision1(playerX, playerY, enemyX, enemyY)
    # if end:
    #     running = False

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
