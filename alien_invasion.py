import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from spaceship import Spaceship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    # Inicializa o jogo e suas configurações de tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    #  Cria instância para armazenar estatísticas do jogo e cria painel de pontuação 
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats) 

    # Cria um objeto para a tela 
    spaceship = Spaceship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    
    # Teste
    #ai_settings.bullet_width = 500
    #ai_settings.fleet_drop_speed = 100
    #ai_settings.alien_speed_factor = 0.5

    # Cria uma frota de alienígenas
    aliens = Group()
    gf.create_fleet(ai_settings, screen, spaceship, aliens)
    
    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, stats, sb, play_button, spaceship, aliens, bullets)

        if stats.game_active:

            # Movimenta a aeronave 
            spaceship.update()

            # Controla os disparos da aeronave
            gf.update_bullets(ai_settings, screen, stats, sb, spaceship, aliens, bullets)

            # Controla a movimentação dos alienígenas
            gf.update_aliens(ai_settings, screen, stats, sb, spaceship, aliens, bullets)

        # Atualiza as imagens na tela e alterna para a nova tela.
        gf.update_screen(ai_settings, screen, stats, sb, spaceship, aliens, bullets, play_button)


run_game()
