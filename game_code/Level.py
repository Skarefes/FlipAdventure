import random

import pygame

from game_code.Const import MENU_OPTION, COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, ENEMY_SCALE
from game_code.EntityFactory import EntityFactory
from pygame.font import Font
from pygame import Surface, Rect


class Level:
    # Classe e construtor de dentro do jogo
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo para selecionar
        self.entity_list = []  # Lista de entidades
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # lista dos imports das imagens para por no level
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # Colocar um unico elemento que é o player1
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(
                EntityFactory.get_entity('Player2'))  # Colocando o segundo player e colcoando pela factoryEntity
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Colocando um timer, para aparecer os inimigos

    def run(self):
        # Para rodar a musica e colocar um clock, que deixa o desempenho do jogo da forma que escolhermos, no caso em 60 FPS
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        # Enquanto ele tiver rodando ele faz pegar e desenha na posição definida pelo retangulo
        while True:
            clock.tick(60)
            # Atualiza a posição da entidade
            # Atualiza a tela com que foi desenhado com o blit
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Evento que faz os inimigos aparecerem aleatoriamente
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity("Enemy1", ENEMY_SCALE))

            # Print dos textos em tela, que são o tempo, fps e quantas entidades tem em tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.1f}s', COLOR_WHITE, (25, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_suft: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_suft.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_suft, text_rect)
