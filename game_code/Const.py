import pygame

# C
COLOR_ORANGE = (255, 85, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 135)
COLOR_GREEN = (0, 90, 0)
COLOR_YELLOW = (211, 211, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_MAGENTA = (255, 0, 255)
COLOR_RED = (230, 0, 0)

CHAR_SCALE = (40, 49)

# E
EVENT_ENEMY = pygame.USEREVENT + 1 # Para aumentar e ocorrer o evento 1, que são os inimigos
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENEMY_SCALE = (45, 49)

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
    'Enemy1': 4,
}

ENTITY_HEALTH = {
    'Bg0': 999,
    'Bg1': 999,
    'Bg2': 999,
    'Bg3': 999,
    'Bg4': 999,
    'Bg5': 999,
    'Bg6': 999,
    'Bg7': 999,
    'Bg8': 999,
    'Player1': 10,
    'Player2': 10,
    'Enemy1': 1
}

ENTITY_DAMAGE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Bg5': 0,
    'Bg6': 0,
    'Bg7': 0,
    'Bg8': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 1
}

ENTITY_SCORE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Bg5': 0,
    'Bg6': 0,
    'Bg7': 0,
    'Bg8': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 1
}

# G
GRAVITY = 0.6

# H
HEIGHT_MAX = 270

# J
JUMP_S = -15

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
SPAWN_TIME = 900
SPEED_SPAWN_TIME = 700

# T
TIMEOUT_LEVEL = 16000
TIMEOUT_STEP = 100

# W
WIN_WIDTH = 900
WIN_HEIGHT = 400

# S
SCORE_POS = {
    'Titulo': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 88),
    'Label': (WIN_WIDTH / 2, 90),
    'Nome': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}