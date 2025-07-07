import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, K_BACKSPACE

from game_code.Const import COLOR_CYAN, SCORE_POS, COLOR_MAGENTA, COLOR_WHITE, MENU_OPTION, COLOR_ORANGE, WIN_HEIGHT, \
    WIN_WIDTH, COLOR_YELLOW, COLOR_RED
from game_code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        imagem_score = pygame.image.load('./asset/Score.png').convert_alpha()
        self.surf = pygame.transform.scale(imagem_score, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):  # Quando salvar aparecerá a tela       #
        #Parar a musica anterior
        pygame.mixer.music.stop()
        # Se terminar e vencer, vai salvar e tocar a musica da vitória
        victory_sound = pygame.mixer.Sound('./asset/Victory-sound.mp3')
        victory_sound.play()
        db_proxy = DBProxy('DBScore')  # Banco de dados chamado DBScore
        nome = ''  # Local que ficara o nome

        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(40, "Parabens pela vitória !!", COLOR_CYAN, SCORE_POS['Titulo'])
            self.score_text(18, "Feito Por: Roger Yamassaki", COLOR_ORANGE,
                            (WIN_WIDTH / 2 - 220, WIN_HEIGHT / 2 + 140))
            self.score_text(15, "RU: 4674958", COLOR_YELLOW,
                            (WIN_WIDTH / 2 - 300, WIN_HEIGHT / 2 + 160))

            if game_mode == MENU_OPTION[0]:  # Se for de um jogador
                score = player_score[0]
                text = 'Player 1 coloque seu nome [Max 5 letras]:'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1])  # Para salvar os scores do player 1 e 2 e divide por 2
                text = 'Coloque o nome do time [Max 5 letras]:'

            self.score_text(20, text, COLOR_MAGENTA, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # Evento para usar o teclado
                    try: # Quando ele tentar digitar
                        if event.key == K_RETURN and len(
                                nome) == 5:  # Se a tecla digitado foi um enter(return) e o tamanho de 5 caracteres ele salva
                            db_proxy.save(
                                {'name': nome, 'score': score,
                                 'date': get_formatted_date()})  # Este get ele pega a data atual
                            self.show()
                            return
                        elif event.key == K_BACKSPACE:
                            nome = nome[:-1]  # Vai apagar uma letra
                        else:
                            if len(nome) < 5:  # se for qualquer tecla menor que 5 ele pega para complementar o nome
                                nome += event.unicode
                    except Exception as e: # Caso haver um erro, ele vai entrar na exceção e mostra no pycharm o erro, e para o jogador, nao acontecerá nada, até ele escrever conforme esta pedido
                        print("Ocorreu um erro", e)
            self.score_text(20, nome, COLOR_WHITE, SCORE_POS['Nome'])
            pygame.display.flip()
            pass

    def show(self):  # Metodo que mostra o Score
        pygame.mixer.music.load('./asset/menu.mp3')
        pygame.mixer.music.play(-1)
        self.window.blit(self.surf, self.rect)  # Desenhar a imagem
        self.score_text(48, 'TOP 10', COLOR_CYAN, SCORE_POS['Titulo'])
        self.score_text(20, 'NAME     SCORE     DATE ', COLOR_MAGENTA, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.top10()  # Puxar o metodo top10
        db_proxy.close()

        for player_score in list_score:  # Correr pela lista e mostrar cada texto em ordem
            id, nome, score, date = player_score
            self.score_text(20, f'  {nome}      {score}    {date}', COLOR_MAGENTA,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, Text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Metodo para escrever
        from pygame.font import Font
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', Text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


def get_formatted_date():  # Pegar a data de hoje
    current_dataline = datetime.now()  # Pegar a data atual
    current_date = current_dataline.strftime("%d/ %m/ %y")  # Pegar dia,mes e ano
    return f'{current_date}'
