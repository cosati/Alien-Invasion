import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.lturn = pygame.image.load('images/lship.bmp')
        self.rturn = pygame.image.load('images/rship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        self.horizontal = float(self.rect.centery)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.horizontal -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.horizontal += self.ai_settings.ship_speed_factor

        # Atualiza  objeto rect de acordo com self.center
        self.rect.centerx = self.center
        self.rect.centery = self.horizontal

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.screen.blit(self.rturn, self.rect)
        elif self.moving_left and self.rect.left > 0:
            self.screen.blit(self.lturn, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
