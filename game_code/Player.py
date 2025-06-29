import pygame
from pygame.examples.moveit import HEIGHT

from game_code.Const import PLAYER_KEY_UP, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT, \
    WIN_WIDTH
from game_code.Entity import Entity


# Classe do Player que vai herdar Entity
class Player(Entity):
    # O construtor contem o nome, a posição e o tamanho que eu desejar
    def __init__(self, name: str, position: tuple, size: tuple):
        super().__init__(name, position, size)

    # Metodo que faz os movimentos dos personagens
    def move(self):
        press_key = pygame.key.get_pressed()  # Enquanto pressionado a tecla, ele fára algo
        # Para ir para cima, baixo, direita ou esquerda e não ultrapasse o cenario
        # self.name vai pegar o player 1 e o 2
        if press_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        #if press_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            #self.rect.centery += ENTITY_SPEED[self.name]
        #Ficar, no chao e o detectar

        #Para andar para os lados
        if press_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if press_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
