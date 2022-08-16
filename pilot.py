import pygame

# Responsável pela maior parte do comportamento do piloto.
class Pilot():
    
    # Inicializa o piloto e define sua posição inicial
    def __init__(self, screen):
        self.screen = screen

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/pilot.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.center = self.screen_rect.center

    # Desenha a espaçonave em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)