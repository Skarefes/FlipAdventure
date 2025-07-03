import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from game_code.Const import COLOR_GREEN, WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_BLACK, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        # Carregar a imagem original, e arrumar a escala da imagem com o transform.scale
        imagem_menu = pygame.image.load('./asset/game_background_2.png').convert_alpha()
        self.surf = pygame.transform.scale(imagem_menu, (WIN_WIDTH, WIN_HEIGHT))

        self.rect = self.surf.get_rect(left=0, top=0)

    # Função que inicia o Menu
    def run(self, ):
        menu_option = 0
        # Para carregar e executar a musica de forma repetitiva
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer.music.play(-1)

        # Enquanto tiver rodando ele mostrará a tela
        while True:
            # menu dos textos com seus tamanhos, cores e tipos
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Flip", COLOR_GREEN, ((WIN_WIDTH / 2), 90))
            self.menu_text(40, "Adventure", COLOR_GREEN, ((WIN_WIDTH / 2), 150))
            # Menu de leitura que quando selecionar muda o texto
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GREEN, ((WIN_WIDTH / 2), 200 + 50 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 200 + 50 * i))
            pygame.display.flip()

            # Check de todos os eventos do Menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:  # Evento para clicar o teclado
                    if event.key == pygame.K_DOWN:  # Quando clicado ele vai para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Evento que faz ir para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Evento que faz apertar o enter e acessar
                        return MENU_OPTION[menu_option]

    # Textos para o menu, para alterar a fonte, a cor o tipo de texto
    def menu_text(self, Text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        from pygame.font import Font
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', Text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
