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
COLOR_ORANGE = (255, 100, 50)
COLOR_WHITE = (255, 255, 255)
COLOR_RAINBOW = gerar_cor_rainbow()

# E

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 3,
    'Player2': 3,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_RETURN}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
