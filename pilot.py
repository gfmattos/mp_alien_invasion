import pygame
from pygame.sprite import Sprite

# Responsável pela maior parte do comportamento do piloto.
class Pilot(Sprite):
    
    # Inicializa o piloto e define sua posição inicial
    def __init__(self, ai_settings, screen):
        super().__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/pilot.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


    # Desenha a espaçonave em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)