# Armazena dados estatísticos da Invasão Alienígena.
class GameStats():
    
    # Inicializa os dados estatísticos
    def __init__(self, ai_settings):
        
        # Inicia a Invasão Alienígena em um estado ativo 
        self.game_active = True

        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia o jogo em um estado inativo
        self.game_active = False

    # Inicializa os dados estatísticos que podem mudar durante o jogo.
    def reset_stats(self):
        
        self.ships_left = self.ai_settings.ship_limit
        