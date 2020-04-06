import sys
import pygame

from bullet import Bullet
from alien import Alien


def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número de alienigenas que cabem em uma linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    # Cria um alienigena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    # Cria um projétil e o adiciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move a espaçonave para a esquerda
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move a espaçonave para cima
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move a espaçonave para baixo
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Responde aeventos de pressionamento de teclas e de moouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    # Redesenha todos os projéteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Deixa a tela mais recente visivel
    pygame.display.flip()


def create_fleet(ai_settings, screen, aliens):
    """Cria uma frota completa de alienígenas"""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # Cria a primeira linha de alienígenas
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
