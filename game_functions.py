import sys
import pygame
from bullet import Bullet


# Responde a eventos de pressionamento de teclas
def check_keydown_events(event, ai_settings, screen, spaceship, bullets):

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

    # Cria o disparo da aeronave
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spaceship, bullets)


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



def check_events(ai_settings, screen, spaceship, bullets):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spaceship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)


# Atualiza as imagens na tela e alterna para a nova tela.
def update_screen(ai_settings, screen, spaceship, pilot, bullets):

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color) 
    spaceship.blitme()
    pilot.blitme()

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
        spaceship.blitme()

    # Deixa a tela mais recente visível 
    pygame.display.flip()


# Atualiza a posição dos projéteis e se livra dos projéteis antigos.
def update_bullets(bullets):

    # Atualiza as posições dos projéteis 
    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy(): 
            if bullet.rect.bottom <= 0: 
                bullets.remove(bullet)


# Cria o disparo da aeronave
def fire_bullet(ai_settings, screen, spaceship, bullets):

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, spaceship)
        bullets.add(new_bullet)