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

        # A pontuação máxima jamais deverá ser reiniciada 
        self.high_score = load_scores()


    # Inicializa os dados estatísticos que podem mudar durante o jogo.
    def reset_stats(self):
        
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


# Carrega a pontuação máxima
def load_scores():
        
    scores = []

    filepath = 'scores.txt'

    with open(filepath, 'r') as file_object:
        lines = file_object.readlines()
        for line in lines:
            scores.append(int(line))

    h_score = max(scores)
        
    return h_score
