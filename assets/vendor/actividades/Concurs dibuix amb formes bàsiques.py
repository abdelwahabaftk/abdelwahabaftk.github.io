import pygame

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

# Colors
GROC = (255, 255, 0)
NEGRE = (0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #  cuerpo
    pygame.draw.circle(pantalla, GROC, (350, 300), 150)
     #boca
    pygame.draw.polygon(pantalla, NEGRE, [(350, 300), (500, 200), (500, 400)])
    # ojo
    pygame.draw.circle(pantalla, NEGRE, (350, 250), 15)
    pygame.display.update()