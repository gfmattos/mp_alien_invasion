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

        # Configurações dos projéteis 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 230, 240)
        self.bullets_allowed = 3
        
    def blue_screen(self):
        self.bg_color = (32, 65, 107) 