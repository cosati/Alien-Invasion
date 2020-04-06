class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (48, 48, 48)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5

        # Configuração dos projéteis
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3
