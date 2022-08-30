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
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # Configurações dos alienígenas
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # Direita = 1 e Esquerda = -1

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    
    # "Inicializa as configurações que mudam no decorrer do jogo
    def initialize_dynamic_settings(self):

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        self.fleet_direction = 1


    # Aumenta as configurações de velocidade
    def increase_speed(self):

        #self.ship_speed_factor *= self.speedup_scale 
        #self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale


    def blue_screen(self):
        self.bg_color = (32, 65, 107) 