import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE, ALT)

NEGRE = (0,0,0)
BLANC = (255,255,255)
VERMELL = (255,0,0)
GROC = (255,255,0)
VERD = (0,180,0)
BLAU = (0,0,255)
MARRON = (139,69,19)
ROSA = (255,150,150)
TARONJA = (255,165,0)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Dibuix')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((135,206,235))  # cielo azul claro

    # Herba
    pygame.draw.rect(pantalla, VERD, (0,450,600,150))

    # Casa
    pygame.draw.rect(pantalla, (255,255,200), (200,300,200,150))

    # Sostre
    pygame.draw.polygon(pantalla, VERMELL, [(200,300),(400,300),(300,230)])

    # Porta
    pygame.draw.rect(pantalla, MARRON, (275,370,50,80))

    # Finestres
    pygame.draw.rect(pantalla, BLAU, (220,320,50,50))
    pygame.draw.rect(pantalla, BLAU, (330,320,50,50))

    # Sol (arriba derecha)
    pygame.draw.circle(pantalla, GROC, (520,100),50)

    # Núvols
    pygame.draw.circle(pantalla, BLANC, (100,100),30)
    pygame.draw.circle(pantalla, BLANC, (130,100),30)
    pygame.draw.circle(pantalla, BLANC, (115,80),30)

    # Arc de Sant Martí (izquierda)
    pygame.draw.arc(pantalla, VERMELL, (50,200,250,200), 3.14, 6.28, 6)
    pygame.draw.arc(pantalla, TARONJA, (60,210,230,180), 3.14, 6.28, 6)
    pygame.draw.arc(pantalla, GROC, (70,220,210,160), 3.14, 6.28, 6)
    pygame.draw.arc(pantalla, VERD, (80,230,190,140), 3.14, 6.28, 6)
    pygame.draw.arc(pantalla, BLAU, (90,240,170,120), 3.14, 6.28, 6)

    # Persona gran (derecha de la casa)
    pygame.draw.circle(pantalla, ROSA, (450,380),20)
    pygame.draw.line(pantalla, NEGRE, (450,400),(450,450),3)
    pygame.draw.line(pantalla, NEGRE, (450,420),(430,440),3)
    pygame.draw.line(pantalla, NEGRE, (450,420),(470,440),3)
    pygame.draw.line(pantalla, NEGRE, (450,450),(430,480),3)
    pygame.draw.line(pantalla, NEGRE, (450,450),(470,480),3)

    # Persona petita
    pygame.draw.circle(pantalla, ROSA, (500,400),15)
    pygame.draw.line(pantalla, NEGRE, (500,415),(500,450),3)
    pygame.draw.line(pantalla, NEGRE, (500,430),(485,445),3)
    pygame.draw.line(pantalla, NEGRE, (500,430),(515,445),3)

    pygame.display.update()

