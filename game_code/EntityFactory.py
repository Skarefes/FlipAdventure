from game_code.Background import Background
from game_code.Const import WIN_WIDTH, WIN_HEIGHT, CHAR_SCALE
from game_code.Player import Player


class EntityFactory:
    #usando o metodo estatico com o design pattern factory, que será uma fabrica de criação do background, personagens e inimgos
    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range (9): # vai ler os cenarios, colocar as posições e as escalas
                    list_bg.append(Background(f'Bg{i}', (0,0), (WIN_WIDTH, WIN_HEIGHT)))
                    list_bg.append(Background(f'Bg{i}', (WIN_WIDTH,0), (WIN_HEIGHT, WIN_HEIGHT)))
                return list_bg
            case 'Player1':
                return Player("Player1", (15, WIN_HEIGHT/2 - 40), CHAR_SCALE)
            case 'Player2':
                return Player("Player2", (8, WIN_HEIGHT/2 - 40), CHAR_SCALE)
        return None
