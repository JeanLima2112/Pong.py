import pygame
from pygame.locals import *
from OpenGL.GL import *

LARGURA_JANELA = 640
ALTURA_JANELA = 480

ydabola = 0
xdabola = 0
tamanhobola = 20
velocidadedabolaemx = 1
velocidadedabolaemy = 1

ydojogador1 = 0
ydojogador2 = 0


def xdojogador1():
    return -LARGURA_JANELA / 2 + larguradosjogadores() / 2

def xdojogador2():
    return LARGURA_JANELA / 2 - larguradosjogadores() / 2

def larguradosjogadores():
    return tamanhobola

def alturadosjogadores():
    return 3 * tamanhobola

def atualizar():
    global xdabola, ydabola, velocidadedabolaemx, velocidadedabolaemy, ydojogador1, ydojogador2

    xdabola = xdabola + velocidadedabolaemx
    ydabola = ydabola + velocidadedabolaemy

    if (xdabola + tamanhobola / 2 > xdojogador2() - larguradosjogadores() / 2
            and ydabola - tamanhobola / 2 < ydojogador2 + alturadosjogadores() / 2
            and ydabola + tamanhobola / 2 > ydojogador2 - alturadosjogadores() / 2):
        velocidadedabolaemx = -velocidadedabolaemx

    if (xdabola - tamanhobola / 2 < xdojogador1() + larguradosjogadores() / 2
            and ydabola - tamanhobola / 2 < ydojogador1 + alturadosjogadores() / 2
            and ydabola + tamanhobola / 2 > ydojogador1 - alturadosjogadores() / 2):
        velocidadedabolaemx = -velocidadedabolaemx

    if ydabola + tamanhobola / 2 > ALTURA_JANELA / 2:
        velocidadedabolaemy = -velocidadedabolaemy

    if ydabola - tamanhobola / 2 < -ALTURA_JANELA / 2:
        velocidadedabolaemy = -velocidadedabolaemy

    if xdabola < -LARGURA_JANELA / 2 or xdabola > LARGURA_JANELA / 2:
        xdabola = 0
        ydabola = 0

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        ydojogador1 = ydojogador1 + 5

    if keys[K_s]:
        ydojogador1 = ydojogador1 - 5

    if keys[K_UP]:
        ydojogador2 = ydojogador2 + 5

    if keys[K_DOWN]:
        ydojogador2 = ydojogador2 - 5

def desenharretangulo(x,y,largura,altura,r,g,b):
    glColor(r,g,b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()
def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharretangulo(xdabola, ydabola, tamanhobola, tamanhobola, 1, 1, 0)
    desenharretangulo(xdojogador1(), ydojogador1, larguradosjogadores(), alturadosjogadores(), 1, 0, 0)
    desenharretangulo(xdojogador2(), ydojogador2, larguradosjogadores(), alturadosjogadores(), 0, 0, 1)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA),DOUBLEBUF | OPENGL)
while True:
    atualizar()
    desenhar()
    pygame.event.pump()

