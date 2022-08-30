# Armazena todas as configurações da Invasão Alienígena.
class Settings():

    # Inicializa as configurações do jogo
    def __init__(self):
        # Configurações da tela 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Configurações da espaçonave 
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configurações dos projéteis 
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Configurações dos alienígenas
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # Direita = 1 e Esquerda = -1

        
    def blue_screen(self):
        self.bg_color = (32, 65, 107) 