import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from spaceship import Spaceship

def run_game():

    # Inicializa o jogo e suas configurações de tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria um objeto para a tela 
    spaceship = Spaceship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    # Cria uma frota de alienígenas
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    
    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, spaceship, bullets)

        # Movimenta a aeronave
        spaceship.update()

        # Controla os disparos da aeronave
        gf.update_bullets(bullets)

        # Atualiza as imagens na tela e alterna para a nova tela.
        gf.update_screen(ai_settings, screen, spaceship, aliens, bullets)


run_game()
