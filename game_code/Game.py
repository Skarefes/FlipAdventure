import pygame

from game_code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from game_code.Level import Level
from game_code.Menu import Menu


class Game:
    # Construtor da classe Game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # função que inicializa o game
    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0]  # Score do Player1 e Player2
                level = Level(self.window, "Level1", menu_return, player_score)
                level_return = level.run(player_score)
            elif menu_return == MENU_OPTION[2]:
                pass
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass
