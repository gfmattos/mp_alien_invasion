import sys
import pygame


# Responde a eventos de pressionamento de teclas e de mouse.
def check_events(spaceship):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Controla o movimento da aeronave
        
        elif event.type == pygame.KEYDOWN:
            # Move a espaçonave para a direita ou para esquerda
            if event.key == pygame.K_RIGHT: 
                spaceship.moving_right = True
            elif event.key == pygame.K_LEFT: 
                spaceship.moving_left = True

        elif event.type == pygame.KEYUP: 
            # Interrompe o movimento
            if event.key == pygame.K_RIGHT:
                spaceship.moving_right = False
            elif event.key == pygame.K_LEFT: 
                spaceship.moving_left = False


# Atualiza as imagens na tela e alterna para a nova tela.
def update_screen(ai_settings, screen, ship, pilot):

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color) 
    ship.blitme()
    pilot.blitme()
    # Deixa a tela mais recente visível 
    pygame.display.flip()


# 