import sys
import pygame
from bullet import Bullet
from alien import Alien


# Responde a eventos de pressionamento de teclas
def check_keydown_events(event, ai_settings, screen, spaceship, bullets):

    # Controla o movimento da aeronave
    # Move a espaçonave para a direita ou para esquerda
    if event.key == pygame.K_RIGHT: 
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT: 
        spaceship.moving_left = True

    # Cria o disparo da aeronave
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spaceship, bullets)

    elif event.key == pygame.K_q: 
        sys.exit() 


# Responde a eventos de solturas de teclas
def check_keyup_events(event, spaceship):

    # Controla o movimento da aeronave   
    # Interrompe o movimento para a direita ou para esquerda
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT: 
        spaceship.moving_left = False


# Verifica os eventos que serão apresentados na atualização da tela
def check_events(ai_settings, screen, spaceship, bullets):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spaceship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)


# Atualiza as imagens na tela e alterna para a nova tela.
def update_screen(ai_settings, screen, spaceship, aliens, bullets):

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color) 
    spaceship.blitme()
    aliens.draw(screen)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
        spaceship.blitme()
        aliens.draw(screen)

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


#Cria uma frota completa de alienígenas.
def create_fleet(ai_settings, screen, aliens):

    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Cria um alienígena e o posiciona na linha
    for alien_number in range(number_aliens_x):

        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        
