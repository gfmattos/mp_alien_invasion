import pygame
from pygame.sprite import Sprite

# Uma classe que administra projéteis disparados pela espaçonave
class Bullet(Sprite):
    
    #Cria um objeto para o projétil na posição atual da espaçonave.
    def __init__(self, ai_settings, screen, spaceship):

        super().__init__() 
        self.screen = screen
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor

        # Cria um retângulo para o projétil em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) 
        self.rect.centerx = spaceship.rect.centerx 
        self.rect.top = spaceship.rect.top

        # Armazena a posição do projétil como um valor decimal 
        self.centery = float(self.rect.centery)
    
    # Move o projétil para cima na tela
    def update(self):
        # Atualiza a posição decimal do projétil 
        self.centery -= self.speed_factor
        # Atualiza a posição de rect 
        self.rect.centery = self.centery

    # Desenha o projétil na tela.
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

