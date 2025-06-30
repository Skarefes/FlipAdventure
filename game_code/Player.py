import pygame
from pygame.examples.moveit import HEIGHT

from game_code.Const import PLAYER_KEY_UP, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT, \
    WIN_WIDTH, GRAVITY, JUMP_S
from game_code.Entity import Entity


# Classe do Player que vai herdar Entity
class Player(Entity):
    # O construtor contem o nome, a posição e o tamanho que eu desejar
    def __init__(self, name: str, position: tuple, size: tuple):
        super().__init__(name, position, size)

        # Variáveis que vão conter a fisica do pulo, para ter gravidade
        self.vel_y = 0  # Controle da velocidade vertical
        self.gravity = GRAVITY  # Para puxar o player para o chão
        self.jump_strength = JUMP_S  # Força e tamanho do pulo
        self.is_jumping = False  # No ar não pode pular novamente

    # Metodo que faz os movimentos dos personagens
    def move(self):
        press_key = pygame.key.get_pressed()  # Enquanto pressionado a tecla, ele fára algo
        # Para ir para cima, direita ou esquerda e não ultrapasse o cenario
        # self.name vai pegar o player 1 e o 2
        if press_key[PLAYER_KEY_UP[self.name]] and not self.is_jumping:
            # self.rect.centery -= ENTITY_SPEED[self.name]
            self.vel_y = self.jump_strength
            self.is_jumping = True

        # Colocando gravidade quando pular
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Ficar no chao e o detectar
        if self.rect.bottom >= WIN_HEIGHT - 30:  # Aumento do encalço do chão
            self.rect.bottom = WIN_HEIGHT - 30
            self.rect.centery += ENTITY_SPEED[self.name]
            self.is_jumping = False

        # Para andar para os lados
        if press_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if press_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
