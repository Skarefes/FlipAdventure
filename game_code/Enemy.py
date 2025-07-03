from game_code.Const import ENTITY_SPEED, WIN_WIDTH
from game_code.Entity import Entity


class Enemy(Entity):
    # Classe do inimigo e seu construtor
    def __init__(self, name: str, position: tuple, size: tuple):
        super().__init__(name, position, size)

    def move(self): # metodo que faz ele se movimentar para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]