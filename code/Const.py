import colorsys
import random

import pygame


def gerar_cor_rainbow():
    hue = random.random()

    saturation = 1
    lightness = 0.5

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, lightness)
    return int(r * 255), int(g * 255), int(b * 255)  # RGB


# C
C_ORANGE = (255, 100, 50)
C_WHITE = (255, 255, 255)
C_RAINBOW = gerar_cor_rainbow()
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E


ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 90,
    'Enemy2': 40,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 20,
}

ENTITY_SCORE =  {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 50,
    'Enemy1Shot': 0,
    'Enemy2': 75,
    'Enemy2Shot': 0,
}

ENTITY_HEALTH = {
    'Level1Bg0': 100,
    'Level1Bg1': 100,
    'Level1Bg2': 100,
    'Level1Bg3': 100,
    'Level1Bg4': 100,
    'Player1': 80,
    'Player1Shot': 1,
    'Player2': 80,
    'Player2Shot': 1,
    'Enemy1': 80,
    'Enemy1Shot': 1,
    'Enemy2': 80,
    'Enemy2Shot': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P

PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_RETURN}

# S
SPAW_TIME = 5000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
