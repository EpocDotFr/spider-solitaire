import sys
import os

# ----------------------------------------------------------------------
# Editable settings

FPS = 30

PILES = 10

CARDS_WIDTH = 70
CARDS_HEIGHT = 101
CARDS_HORIZONTAL_MARGIN = 5
CARDS_VERTICAL_MARGIN = 10
CARDS_INITIAL_DEAL = 54
CARDS_PER_DEAL = 10

WINDOW_PADDING = 10

MUSIC_VOLUME = 0.2
SOUNDS_VOLUME = 0.3

# ----------------------------------------------------------------------
# Game constants - do not edit anything after this line

# When frozen by PyInstaller, the path to the resources is different
RESOURCES_ROOT = os.path.join(sys._MEIPASS, 'resources') if getattr(sys, 'frozen', False) else 'resources'

TABLEAU_TOP = WINDOW_PADDING + CARDS_HEIGHT + CARDS_VERTICAL_MARGIN

WINDOW_SIZE = (
    PILES * CARDS_WIDTH + (PILES - 1) * CARDS_HORIZONTAL_MARGIN + WINDOW_PADDING * 2,
    TABLEAU_TOP + CARDS_HEIGHT * 8 # TODO 8: arbitrary number
)
