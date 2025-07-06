from abc import ABC, abstractmethod

import pygame

from game_code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


#Classe abstract
class Entity(ABC):
    #Construtor da super classe
    def __init__(self, name: str, position: tuple, size = None):
        self.name = name
        #Carregar os cenarios e personagens
        cenario_original = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        #Se o size tiver alguma escala alterada manualmente ele mostra, se não vai o original
        if size is not None:
            self.surf = pygame.transform.scale(cenario_original, size)
        else:
            self.surf = cenario_original
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod #Metodo abstrato
    def move(self):
        pass