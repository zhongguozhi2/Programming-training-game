import pygame
from pygame.locals import *

# initialize 英 /ɪ'nɪʃ(ə)laɪz/ 初始化
pygame.init()


surface = pygame.display.set_mode((1000, 600))
icon_img = pygame.image.load(r"C:\Users\小志志\Desktop\209AA17C4EEDEC161B3F779E3DA3BB25.jpg")
pygame.display.set_icon(icon_img)
pygame.display.set_caption("让我们一起学习pygame吧！！！")
# pygame.display.set_palette()

background_img = pygame.image.load(r"C:\Users\小志志\PycharmProjects\thesis\img\game1.jpg")
while True:
    surface.blit(background_img, (0, 0))
    pygame.display.update()

