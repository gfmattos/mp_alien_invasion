import pygame
from pygame.sprite import Sprite

# Uma classe que representa um único alienígena da frota.
class Alien(Sprite):
    
    # Inicializa o alienígena e define sua posição inicial.
    def __init__(self, ai_settings, screen):

        super().__init__() 
        self.screen = screen 
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect 
        self.image = pygame.image.load('images/alien.bmp') 
        self.rect = self.image.get_rect()
        
        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena 
        self.x = float(self.rect.x)


    # Desenha o alienígena em sua posição atual.
    def blitme(self):
        self.screen.blit(self.image, self.rect)
