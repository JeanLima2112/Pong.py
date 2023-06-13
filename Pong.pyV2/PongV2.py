import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura =640
altura = 480
x = y = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pong.py')
relogio = pygame.time.Clock()
while True:
    relogio.tick(24)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela,(255,255,255),(x,y,40,50))

    pygame.display.update()
