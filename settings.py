import sys
import os

# ----------------------------------------------------------------------
# Editable settings

FPS = 30
CARDS_WIDTH = 70
CARDS_HEIGHT = 101
TABLEAU_COLS = 10

# ----------------------------------------------------------------------
# Game constants - do not edit anything after this line

# When frozen by PyInstaller, the path to the resources is different
RESOURCES_ROOT = os.path.join(sys._MEIPASS, 'resources') if getattr(sys, 'frozen', False) else 'resources'

CARDS = {
    'ace': 13,
    'king': 12,
    'queen': 11,
    'jack': 10,
    '10': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

CARDS_VARIANTS = ['spades', 'hearts', 'diamonds', 'clubs']

WINDOW_SIZE = (
    800,
    600
)
