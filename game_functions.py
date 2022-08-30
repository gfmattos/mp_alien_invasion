import sys
import pygame
from time import sleep
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
def check_events(ai_settings, screen, stats, play_button, spaceship, aliens, bullets):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spaceship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            check_play_button(ai_settings, screen, stats, play_button, spaceship, aliens, bullets, mouse_x, mouse_y)


# Inicia um novo jogo quando o jogador clicar em Play."
def check_play_button(ai_settings, screen, stats, play_button, spaceship, aliens, bullets, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 

    if button_clicked and not stats.game_active:

        # Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()

        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()

        stats.game_active = True

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, spaceship, aliens) 
        spaceship.center_ship()


# Atualiza as imagens na tela e alterna para a nova tela.
def update_screen(ai_settings, screen, stats, spaceship, aliens, bullets, play_button):

    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color) 
    spaceship.blitme()
    aliens.draw(screen)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
        spaceship.blitme()
        aliens.draw(screen)

    # Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active: 
        play_button.draw_button()

    # Deixa a tela mais recente visível 
    pygame.display.flip()


# Atualiza a posição dos projéteis e se livra dos projéteis antigos.
def update_bullets(ai_settings, screen, spaceship, aliens, bullets):

    # Atualiza as posições dos projéteis 
    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy(): 
            if bullet.rect.bottom <= 0: 
                bullets.remove(bullet)

    # Verifica se algum projétil atingiu os alienígenas
    # Em caso afirmativo, livra-se do projétil e do alienígena
    check_bullet_alien_collisions(ai_settings, screen, spaceship, aliens, bullets)


# Responde a colisões entre projéteis e alienígenas.
def check_bullet_alien_collisions(ai_settings, screen, spaceship, aliens, bullets):

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # Destrói projéteis existentes, aumenta a velocidade do jogo e cria nova frota
    if len(aliens) == 0:
        ai_settings.increase_speed()
        bullets.empty()
        create_fleet(ai_settings, screen, spaceship, aliens)


# Cria o disparo da aeronave
def fire_bullet(ai_settings, screen, spaceship, bullets):

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, spaceship)
        bullets.add(new_bullet)


#Cria uma frota completa de alienígenas.
def create_fleet(ai_settings, screen, spaceship, aliens):

    # Cria um alienígena e calcula o número de alienígenas em uma linha
    # O espaçamento entre os alienígenas é igual à largura de um alienígena

    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, spaceship.rect.height, alien.rect.height)

    # Cria um alienígena e o posiciona na linha
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number) 


# Determina o número de alienígenas que cabem em uma linha
def get_number_aliens_x(ai_settings, alien_width):
    
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    
    return number_aliens_x


# Determina o número de linhas com alienígenas que cabem na tela
def get_number_rows(ai_settings, ship_height, alien_height): 

    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height) 
    number_rows = int(available_space_y / (2 * alien_height)) 
    
    return number_rows


# Cria um alienígena e o posiciona na linha
def create_alien(ai_settings, screen, aliens, alien_number, row_number):

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien_height + 2 * alien_height * row_number 
    aliens.add(alien)


# Responde ao fato de a espaçonave ter sido atingida por um alienígena
def ship_hit(ai_settings, stats, screen, spaceship, aliens, bullets):

    if stats.ships_left > 0: 
        # Diminui o número de aeronaves 
        stats.ships_left -= 1
    
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, spaceship, aliens) 
        spaceship.center_ship()

        # Faz uma pausa
        sleep(1)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# Verifica se algum alienígena alcançou a parte inferior da tela
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites(): 
        if alien.rect.bottom >= screen_rect.bottom: 
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


# Atualiza as posições de todos os alienígenas da frota.
def update_aliens(ai_settings, stats, screen, spaceship, aliens, bullets):

    # Verifica se a frota está em uma das bordas e então atualiza as posições de todos os alienígenas da frota.
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(spaceship, aliens):
        ship_hit(ai_settings, stats, screen, spaceship, aliens, bullets)
    
    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings, stats, screen, spaceship, aliens, bullets)


# Responde apropriadamente se algum alienígena alcançou uma borda
def check_fleet_edges(ai_settings, aliens):
    
    for alien in aliens.sprites(): 
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens) 
            break


# Faz toda a frota descer e muda a sua direção
def change_fleet_direction(ai_settings, aliens):

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed 
    ai_settings.fleet_direction *= -1