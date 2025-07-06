import pygame

from game_code.Const import MENU_OPTION, COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, ENEMY_SCALE, \
    COLOR_GREEN, TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP, ENTITY_SPEED, SPEED_SPAWN_TIME, COLOR_BLUE, COLOR_YELLOW, \
    COLOR_ORANGE
from game_code.Entity import Entity
from game_code.EntityFactory import EntityFactory
from pygame.font import Font
from pygame import Surface, Rect

from game_code.EntityMediator import EntityMediator
from game_code.Player import Player


class Level:
    # Classe e construtor de dentro do jogo
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 16 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo para selecionar
        self.entity_list: list[Entity] = []  # Lista de entidades
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # lista dos imports das imagens para por no level
        player = EntityFactory.get_entity('Player1')  # Vai pegar a entidade player
        player.score = player_score[0]  # jogar o player para contar o score
        self.entity_list.append(player)  # Colocar um unico elemento que é o player1
        if game_mode in [MENU_OPTION[1]]:
            player = EntityFactory.get_entity('Player2')  # Vai pegar a entidade player
            player.score = player_score[1]  # jogar o player para contar o score
            self.entity_list.append(player)  # Colocando o segundo player e colocando pela factoryEntity
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Colocando um timer, para aparecer os inimigos
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Evento de cronometro

    def run(self, player_score: list[int]):
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
                # Mostrando o Score do personagem no jogo
                if isinstance(ent, Player):
                    if ent.name == 'Player1':
                        self.level_text(20, f'HP: {ent.health}|SCORE: {ent.score}', COLOR_GREEN,
                                        (WIN_WIDTH / 2 - 100, 25))
                    if ent.name == 'Player2':
                        self.level_text(20, f'HP: {ent.health}|SCORE: {ent.score}', COLOR_GREEN,
                                        (WIN_WIDTH / 2 - 100, 45))
            # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:  # Evento que faz os inimigos aparecerem aleatoriamente
                    self.entity_list.append(EntityFactory.get_entity("Enemy1", ENEMY_SCALE))
                if event.type == EVENT_TIMEOUT:  # Evento no qual acabar o tempo ocorre algo, como terminar o jogo
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == TIMEOUT_LEVEL // 2: # Se o tempo tiver pela metade
                        pygame.time.set_timer(EVENT_ENEMY, SPEED_SPAWN_TIME) # os inimigos apareceram mais rapido
                    if self.timeout == 0:  # Se o tempo zerar
                        for ent in self.entity_list:  # varrer as entidades
                            if isinstance(ent, Player) and ent.name == 'Player1':  # Se este for entidade player 1
                                player_score[0] = ent.score  # Conta no score do Player1
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score

                        # Pauso a musica de fundo
                        pygame.mixer_music.stop()

                        # Se terminar e vencer, toca a musica de vitória
                        victory_sound = pygame.mixer.Sound('./asset/Victory-sound.mp3')
                        victory_sound.play()

                        # Mostrar tela preta com mensagem de finalização
                        self.window.fill((0, 0, 0))
                        self.level_text(40, "Parabens pela vitória !!", COLOR_YELLOW,
                                        (WIN_WIDTH / 2 - 300, WIN_HEIGHT / 2 - 21))
                        self.level_text(20, "Feito Por: Roger Yamassaki", COLOR_ORANGE,
                                        (WIN_WIDTH / 2 - 240, WIN_HEIGHT / 2 + 45))
                        self.level_text(15, "RU: 4674958", COLOR_YELLOW,
                                        (WIN_WIDTH / 2 - 300, WIN_HEIGHT / 2 + 78))
                        pygame.display.flip()

                        # Tempo de imagem de parabens com nome do autor
                        pygame.time.delay(3000)

                        return True

            found_player = False  # Começa com player encontrado falso
            for ent in self.entity_list:  # Achar o player na lista
                if isinstance(ent, Player):  # Ver se existe a instancia do Player
                    found_player = True
            if not found_player:  # Se não encontrar retorne false e finalize
                death_sound = pygame.mixer.Sound(f'./asset/Death_Sound.mp3')
                death_sound.play()  # Tocar o som quando morrer

                self.level_text(40, "Voce falhou !!", COLOR_BLUE,
                                        (WIN_WIDTH / 2 - 170, WIN_HEIGHT / 2 - 25))
                pygame.display.flip()

                pygame.time.delay(1200)  # Após morrer pausa o jogo por 1 segundo

                pygame.mixer_music.stop()
                return False

            # Print dos textos em tela, que são o tempo, fps e quantas entidades tem em tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.1f}s', COLOR_WHITE, (25, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Colisões, pontuações e vidas
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Para reconhecer a colisão no Level
            EntityMediator.verify_health(entity_list=self.entity_list)  # Para reconhecer a vida das entidades
            EntityMediator.give_score(entity_list=self.entity_list)
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)
        text_suft: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_suft.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_suft, text_rect)
