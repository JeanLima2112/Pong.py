import pygame
from pygame.locals import *
from OpenGL.GL import *
import time
import random

efeitoque = ["Sounds/EFEITOS SONOROS-1.wav","Sounds/EFEITOS SONOROS-2.wav",
             "Sounds/EFEITOS SONOROS-3.wav","Sounds/EFEITOS SONOROS-4.wav",
             "Sounds/EFEITOS SONOROS-5.wav"]

#Musica de Fundo
pygame.mixer.init()
pygame.mixer.music.load("Sounds/❌--Te Assumi Pro Brasil-(SAXOFONE COVER) -Matheus _ Kauan (SAXOFONE COVER)(MP3_320K).mp3")
pygame.mixer.music.set_volume(2)

# efeitos Sonoros
sons = [pygame.mixer.Sound(efeitoque[0]),
        pygame.mixer.Sound(efeitoque[1]),
        pygame.mixer.Sound(efeitoque[2]),
        pygame.mixer.Sound(efeitoque[3]),
        pygame.mixer.Sound(efeitoque[4])]

somponto = pygame.mixer.Sound("Sounds/spell1_0.wav")

LARGURA_JANELA = 680
ALTURA_JANELA = 480

ydabola = 0
xdabola = 0
tamanhobola = 20
velocidadedabolaemx = 0.3
velocidadedabolaemy = 0.1

ydojogador1 = 0
ydojogador2 = 0

pontosj2 = 0
pontosj1 = 0

def xdojogador1():
    return -LARGURA_JANELA / 2 + larguradosjogadores() / 2

def xdojogador2():
    return LARGURA_JANELA / 2 - larguradosjogadores() / 2

def larguradosjogadores():
    return tamanhobola

def alturadosjogadores():
    return 5 * tamanhobola

def atualizar():
    global xdabola, ydabola, velocidadedabolaemx, velocidadedabolaemy, ydojogador1, ydojogador2
    xdabola += velocidadedabolaemx
    ydabola += velocidadedabolaemy

    if (xdabola + tamanhobola / 2 > xdojogador2() - larguradosjogadores() / 2
            and ydabola - tamanhobola / 2 < ydojogador2 + alturadosjogadores() / 2
            and ydabola + tamanhobola / 2 > ydojogador2 - alturadosjogadores() / 2):
        velocidadedabolaemx = -velocidadedabolaemx
        velocidadedabolaemx -= 0.035
        velocidadedabolaemy -= random.random()/4
        random.choice(sons).play()

    if (xdabola - tamanhobola / 2 < xdojogador1() + larguradosjogadores() / 2
            and ydabola - tamanhobola / 2 < ydojogador1 + alturadosjogadores() / 2
            and ydabola + tamanhobola / 2 > ydojogador1 - alturadosjogadores() / 2):
        velocidadedabolaemx = -velocidadedabolaemx
        velocidadedabolaemx += 0.035
        velocidadedabolaemy += random.random()/4
        random.choice(sons).play()

    if ydabola + tamanhobola / 2 > ALTURA_JANELA / 2:
        velocidadedabolaemy = -velocidadedabolaemy

    if ydabola - tamanhobola / 2 < -ALTURA_JANELA / 2:
        velocidadedabolaemy = -velocidadedabolaemy

    if xdabola < -LARGURA_JANELA / 2:

        xdabola = 0
        somponto.play()
        time.sleep(0.7)


        velocidadedabolaemx = - 0.3
        velocidadedabolaemy = - 0.1

    if xdabola > LARGURA_JANELA / 2:
        xdabola = 0
        somponto.play()
        time.sleep(0.7)



        velocidadedabolaemx = 0.3
        velocidadedabolaemy = 0.1

    keys = pygame.key.get_pressed()

    if ydojogador1 + tamanhobola / 2 < +ALTURA_JANELA / 2:
        if keys[K_w]:
            ydojogador1 = ydojogador1 + 1

    if ydojogador1 - tamanhobola / 2 > -ALTURA_JANELA / 2:
        if keys[K_s]:
            ydojogador1 = ydojogador1 - 1

    if ydojogador2 + tamanhobola / 2 < +ALTURA_JANELA / 2:
        if keys[K_UP]:
            ydojogador2 = ydojogador2 + 1

    if ydojogador2 - tamanhobola / 2 > -ALTURA_JANELA / 2:
        if keys[K_DOWN]:
            ydojogador2 = ydojogador2 - 1


def desenharretangulo(x,y,largura,altura,r,g,b):
    glColor(r,g,b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x,0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()
def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharretangulo(xdabola, ydabola, tamanhobola, tamanhobola, 1, 1, 0)
    desenharretangulo(xdojogador1(), ydojogador1, larguradosjogadores(), alturadosjogadores(), 1, 1, 1)
    desenharretangulo(xdojogador2(), ydojogador2, larguradosjogadores(), alturadosjogadores(), 1, 1, 1)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA),DOUBLEBUF | OPENGL)
pygame.display.set_caption("PONG.py")
pygame.mixer.music.play(-1)

while True:
    atualizar()
    desenhar()
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()




