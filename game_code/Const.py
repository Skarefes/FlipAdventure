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
EVENT_ENEMY = pygame.USEREVENT + 1
ENEMY_SCALE = (45,49)

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

# W
WIN_WIDTH = 900
WIN_HEIGHT = 400
