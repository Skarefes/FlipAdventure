import pygame

from game_code.Const import MENU_OPTION
from game_code.EntityFactory import EntityFactory


class Level:
    # Classe e construtor de dentro do jogo
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo para selecionar
        self.entity_list = []  # Lista de entidades
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # lista dos imports das imagens para por no level
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # Colocar um unico elemento que é o player1
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(
                EntityFactory.get_entity('Player2'))  # Colocando o segundo player e colcoando pela factoryEntity

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
            pygame.display.flip()
            pass
