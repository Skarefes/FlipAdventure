from abc import ABC, abstractmethod

import pygame

from game_code.Const import WIN_WIDTH, WIN_HEIGHT


#Classe abstract
class Entity(ABC):
    #Construtor que contem o nome, a imagem que será gerada, sua posição, sua velocidade e sua escala
    def __init__(self, name: str, position: tuple, size = None):
        self.name = name
        #Carregar o cenario, e transformar a scala dele no tamanho que eu precisar da tela, para ficar ajustado
        cenario_original = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        #Se o size tiver alguma escala posta, se não vai original
        if size is not None:
            self.surf = pygame.transform.scale(cenario_original, size)
        else:
            self.surf = cenario_original
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod #Metodo abstrato
    def move(self):
        pass