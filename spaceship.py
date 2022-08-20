import pygame

# Responsável pela maior parte do comportamento da espaçonave do jogador.
class Spaceship():
    
    # Inicializa a espaçonave e define sua posição inicial
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.moving_right = False
        self.moving_left = False

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.centerx = float(self.rect.centerx)
        

    # Flag de movimento. Atualiza a posição da espaçonave de acordo com a flag de movimento.
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0: 
            self.centerx -= self.ai_settings.ship_speed_factor
    
        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.centerx


    # Desenha a espaçonave em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)
