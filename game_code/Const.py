import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLACK = (0, 0, 0)

CHAR_SCALE = (40, 49)

# E
ENTITY_SPEED = {
    'Bg0': 0,
    'Bg1': 1,
    'Bg2': 2,
    'Bg3': 3,
    'Bg4': 4,
    'Bg5': 5,
    'Bg6': 6,
    'Bg7': 6,
    'Bg8': 7,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

# G
GRAVITY = 0.5

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 900
WIN_HEIGHT = 600
