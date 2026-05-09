# JOC DELS METEORITS
# =============================================================================
# Un joc on una nau espacial ha d'esquivar meteorits que cauen del cel.
# El jugador perd una vida cada vegada que un meteorit toca la nau.
# Quan es perden totes les vides, apareix la pantalla de Game Over.
# =============================================================================

import random
import pygame
import time
from pygame.locals import *


# =============================================================================
# CLASSE METEOR
# =============================================================================
class Meteor:

    def __init__(self, imatge, velocitat, pos_x, pos_y):
        self.imatge = imatge
        self.velocitat = velocitat
        self.x = pos_x
        self.y = pos_y
        self.img_meteor = pygame.image.load(self.imatge)
        self.rect_meteor = self.img_meteor.get_rect(midbottom=(self.x, self.y))

    def reiniciar(self):
        self.x = random.randint(30, 610)
        self.y = -64
        self.velocitat = random.randint(2, 10)

    def moure(self):
        self.y += self.velocitat
        self.rect_meteor = self.img_meteor.get_rect(midbottom=(self.x, self.y))

    def ha_sortit_per_baix(self):
        return self.y >= 480

    def puntuar_i_reiniciar(self):
        if self.ha_sortit_per_baix():
            self.reiniciar()
            return 5
        return 0


# =============================================================================
# CLASSE NAU
# =============================================================================
class Nau:

    def __init__(self, imatge, velocitat, pos_x, pos_y, vides, imatge_vida):
        self.imatge = imatge
        self.velocitat = velocitat
        self.x = pos_x
        self.y = pos_y

        self.img = pygame.image.load(self.imatge)
        self.img_vida = pygame.image.load(imatge_vida)

        self.rect = self.img.get_rect(midbottom=(self.x, self.y))

        self.vides = vides
        self.vides_originals = vides

    def reiniciar(self):
        self.x = 300
        self.y = 460
        self.rect = self.img.get_rect(midbottom=(self.x, self.y))
        self.vides = self.vides_originals

    def moure(self, pantalla_rect):
        keys = pygame.key.get_pressed()

        if keys[K_a] or keys[K_LEFT]:
            self.rect.x -= self.velocitat
        if keys[K_d] or keys[K_RIGHT]:
            self.rect.x += self.velocitat
        if keys[K_w] or keys[K_UP]:
            self.rect.y -= self.velocitat
        if keys[K_s] or keys[K_DOWN]:
            self.rect.y += self.velocitat

        self.rect.clamp_ip(pantalla_rect)

    def restar_vida(self):
        self.vides -= 1

    def esta_viva(self):
        return self.vides > 0


# =============================================================================
# CLASSE JOC
# =============================================================================
class Joc:

    PANTALLA_INICI = "inici"
    PANTALLA_JOC = "joc"
    PANTALLA_GAME_OVER = "game_over"

    def __init__(self, ample, alt, fps, nombre_meteors):
        pygame.init()

        self.ample = ample
        self.alt = alt
        self.fps = fps
        self.numero_meteors = nombre_meteors

        self.pantalla = pygame.display.set_mode((self.ample, self.alt))
        pygame.display.set_caption("Joc dels Meteorits")

        self.rellotge = pygame.time.Clock()

        self.meteors = []
        self.punts = 0

        self.nau = Nau('assets/saroghh2.png', velocitat=5, pos_x=300, pos_y=450,
                       vides=3, imatge_vida='assets/corazon.png')

        self.pantalla_activa = self.PANTALLA_INICI

    # -------------------------------------------------------------------------
    # BUCLE PRINCIPAL
    # -------------------------------------------------------------------------
    def iniciar_joc(self):
        while True:
            if self.pantalla_activa == self.PANTALLA_INICI:
                self.mostrar_pantalla_inici()

            elif self.pantalla_activa == self.PANTALLA_JOC:
                self.preparar_partida()
                self.mostrar_pantalla_joc()

            elif self.pantalla_activa == self.PANTALLA_GAME_OVER:
                self.mostrar_pantalla_game_over()

    # -------------------------------------------------------------------------
    # PANTALLA D'INICI
    # -------------------------------------------------------------------------
    def mostrar_pantalla_inici(self):
        img_start = pygame.image.load('assets/start.png')
        self.pantalla.blit(img_start, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                self.pantalla_activa = self.PANTALLA_JOC

        self.rellotge.tick(self.fps)

    # -------------------------------------------------------------------------
    # PANTALLA GAME OVER
    # -------------------------------------------------------------------------
    def mostrar_pantalla_game_over(self):
        img_game_over = pygame.image.load('assets/gameover.png')
        self.pantalla.blit(img_game_over, (0, 0))

        self._dibuixar_text(f"Puntuació: {self.punts}", mida=36, color=(255, 255, 0),
                             x=self.ample // 2, y=380, centrat=True)
        self._dibuixar_text("Prem qualsevol tecla per tornar", mida=22,
                             color=(200, 200, 200), x=self.ample // 2, y=430, centrat=True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.pantalla_activa = self.PANTALLA_INICI

        self.rellotge.tick(self.fps)

    # -------------------------------------------------------------------------
    # PANTALLA DE JOC
    # -------------------------------------------------------------------------
    def mostrar_pantalla_joc(self):
        while self.pantalla_activa == self.PANTALLA_JOC:

            self._gestionar_events()

            self.pantalla.fill((0, 0, 0))

            self.nau.moure(self.pantalla.get_rect())
            self._moure_meteors()

            self._control_colisions()

            self._dibuixar_meteors()
            self._dibuixar_nau()
            self._dibuixar_vides()
            self._dibuixar_punts()

            if not self.nau.esta_viva():
                self.pantalla_activa = self.PANTALLA_GAME_OVER

            pygame.display.update()
            self.rellotge.tick(self.fps)

    # -------------------------------------------------------------------------
    # PREPARACIÓ DE PARTIDA
    # -------------------------------------------------------------------------
    def preparar_partida(self):
        self.meteors.clear()

        for i in range(self.numero_meteors):
            meteor_nou = Meteor('assets/peligroso.png', velocitat=0, pos_x=0, pos_y=0)
            meteor_nou.reiniciar()
            self.meteors.append(meteor_nou)

        self.nau.reiniciar()
        self.punts = 0

    # -------------------------------------------------------------------------
    # LÒGICA INTERNA
    # -------------------------------------------------------------------------
    def _gestionar_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def _moure_meteors(self):
        for meteor in self.meteors:
            meteor.moure()
            self.punts += meteor.puntuar_i_reiniciar()

    def _control_colisions(self):
        for meteor in self.meteors:
            if meteor.rect_meteor.colliderect(self.nau.rect):
                meteor.reiniciar()
                self.nau.restar_vida()

    # -------------------------------------------------------------------------
    # DIBUIX
    # -------------------------------------------------------------------------
    def _dibuixar_meteors(self):
        for meteor in self.meteors:
            self.pantalla.blit(meteor.img_meteor, meteor.rect_meteor)

    def _dibuixar_nau(self):
        self.pantalla.blit(self.nau.img, self.nau.rect)

    def _dibuixar_vides(self):
        posicions_x = [500, 540, 580]
        for i in range(self.nau.vides):
            if i < len(posicions_x):
                self.pantalla.blit(self.nau.img_vida, (posicions_x[i], 20))

    def _dibuixar_punts(self):
        self._dibuixar_text(str(self.punts), mida=32, color=(255, 255, 255),
                             x=140, y=30, centrat=False)

    def _dibuixar_text(self, text, mida, color, x, y, centrat=False):
        font = pygame.font.SysFont(None, mida)
        imatge_text = font.render(text, True, color)

        if centrat:
            rect_text = imatge_text.get_rect(center=(x, y))
            self.pantalla.blit(imatge_text, rect_text)
        else:
            self.pantalla.blit(imatge_text, (x, y))


# =============================================================================
# INICI DEL PROGRAMA
# =============================================================================

partida = Joc(
    ample=640,
    alt=480,
    fps=60,
    nombre_meteors=4
)
partida.iniciar_joc()
