import pygame
import game_functions as gf
from settings import Settings
from spaceship import Spaceship
from pilot import Pilot

def run_game():

    # Inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    ai_settings = Settings()
    ai_settings.blue_screen()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    spaceship = Spaceship(ai_settings, screen)
    pilot = Pilot(screen)

    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        gf.check_events(spaceship)

        # Movimenta a aeronave
        spaceship.update()

        # Atualiza as imagens na tela e alterna para a nova tela.
        gf.update_screen(ai_settings, screen, spaceship, pilot)

run_game()
