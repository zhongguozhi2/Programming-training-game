import pygame
import sys
import time
import random
from pygame.locals import *
import main

pygame.init()
fbsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake go!')
# image = pygame.image.load('game.ico')
# pygame.display.set_icon(image)

redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)
LightGrey = pygame.Color(220, 220, 220)


def gameOver(surface, score):
    gameOverFont = pygame.font.Font('simhei.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColor)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 125)
    surface.blit(gameOverSurf, gameOverRect)
    scoreFont = pygame.font.Font('simhei.ttf', 48)
    scoreSurf = scoreFont.render('SCORE:' + str(score), True, greyColor)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (320, 225)
    surface.blit(scoreSurf, scoreRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


snakePosition = [100, 100]
snakeSegments = [[100, 100], [80, 100], [60, 100]]
raspberryPosition = [300, 300]
raspberrySpawned = 1
direction = 'right'
changeDirction = 'right'
score = 0
start_time = time.time()
while True:

    time1 = main.timer(start_time)


    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.type == ord('d'):
                changeDirction = 'right'
            elif event.key == K_LEFT or event.type == ord('a'):
                changeDirction = 'left'
            elif event.key == K_UP or event.type == ord('w'):
                changeDirction = 'up'
            elif event.key == K_DOWN or event.type == ord('s'):
                changeDirction = 'down'
            elif event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeDirction == 'right' and not direction == 'left':
        direction = changeDirction
    if changeDirction == 'left' and not direction == 'right':
        direction = changeDirction
    if changeDirction == 'up' and not direction == 'down':
        direction = changeDirction
    if changeDirction == 'down' and not direction == 'up':
        direction = changeDirction


    if direction == 'right':
        snakePosition[0] += 20
    elif direction == 'left':
        snakePosition[0] -= 20
    elif direction == 'up':
        snakePosition[1] -= 20
    elif direction == 'down':
        snakePosition[1] += 20
    print(snakePosition)
    snakeSegments.insert(0, list(snakePosition))

    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()


    if raspberrySpawned == 0:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        raspberryPosition = [int(x*20), int(y*20)]
        raspberrySpawned = 1
        score += 1

    surface.fill(blackColor)
    for position in snakeSegments[1:]:
        pygame.draw.rect(surface, whiteColor, Rect(position[0], position[1], 20, 20))
    pygame.draw.rect(surface, LightGrey, Rect(snakePosition[0], snakePosition[1], 20, 20))
    pygame.draw.rect(surface, redColor, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
    gameOverFont = pygame.font.Font('font/simhei.ttf', 25)
    font1 = gameOverFont.render('你已经玩了{}秒,请注意休息！！！'.format(time1), True, (255, 255, 255))

    rect1 = font1.get_rect()
    surface.blit(font1, rect1)
    pygame.display.update()


    if len(snakeSegments) < 40:
        speed = 6 + len(snakeSegments)//4
    else:
        speed = 16
    fbsClock.tick(speed)
