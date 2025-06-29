from game_code.Const import ENTITY_SPEED, WIN_WIDTH
from game_code.Entity import Entity


class Background(Entity): # classe do backgroun que herda de Entity
    def __init__(self, name: str, position: tuple, size = None):
        super().__init__(name, position, size)

    #metodo que faz a posição, o movimento e a velocidade do cenário em relação ao eixo x
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH