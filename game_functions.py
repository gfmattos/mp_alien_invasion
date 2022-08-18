import sys
import pygame


# Responde a eventos de pressionamento de teclas
def check_keydown_events(event, spaceship):

    # Controla o movimento da aeronave
    # Move a espaçonave para a direita ou para esquerda
    if event.key == pygame.K_RIGHT: 
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT: 
        spaceship.moving_left = True
        
    # Move a espaçonave para cima ou para baixo
    #elif event.key == pygame.K_UP: 
    #    spaceship.moving_up = True
    #elif event.key == pygame.K_DOWN: 
    #    spaceship.moving_down = True


# Responde a eventos de solturas de teclas
def check_keyup_events(event, spaceship):

    # Controla o movimento da aeronave   
    # Interrompe o movimento para a direita ou para esquerda
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT: 
        spaceship.moving_left = False

    # Interrompe o movimento para cima ou para baixo
    #elif event.key == pygame.K_UP: 
    #    spaceship.moving_up = False
    #elif event.key == pygame.K_DOWN: 
    #    spaceship.moving_down = False


def check_events(spaceship):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, spaceship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)


# Atualiza as imagens na tela e alterna para a nova tela.
def update_screen(ai_settings, screen, ship, pilot):

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color) 
    ship.blitme()
    pilot.blitme()
    # Deixa a tela mais recente visível 
    pygame.display.flip()


# 