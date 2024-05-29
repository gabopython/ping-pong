import pygame
from pygame.locals import *

WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants
ALTO_BLOQUE = 50
ANCHO_BLOQUE = 200

# variables
bloques = [pygame.Rect(0, HEIGHT - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)]
velocidad = 10
x_previa = 0
w_previa = WIDTH

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bloques[-1].x < x_previa:
                    bloques[-1].w -= abs(bloques[-1].x - x_previa)
                    bloques[-1].x = x_previa
                elif bloques[-1].x + bloques[-1].w > x_previa + w_previa:
                    bloques[-1].w -= abs(bloques[-1].x - x_previa)
                bloques.append(
                    pygame.Rect(
                        bloques[-1].x,
                        bloques[-1].y - ALTO_BLOQUE,
                        bloques[-1].w,
                        ALTO_BLOQUE,
                    )
                )
                x_previa = bloques[-1].x
                w_previa = bloques[-1].w
    # code here

    bloques[-1].x += velocidad
    if bloques[-1].x + bloques[-1].w > WIDTH:
        velocidad = -velocidad
    if bloques[-1].x < 0:
        velocidad = -velocidad

    for bloque in bloques:
        pygame.draw.rect(screen, (255, 255, 255), bloque)

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)
