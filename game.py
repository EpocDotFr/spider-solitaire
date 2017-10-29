import settings
import logging
import helpers
import random
import pygame
import math
import cards
import sys


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.DOUBLEBUF)
        self.window_rect = self.window.get_rect()

        pygame.display.set_caption('Spider Solitaire')
        pygame.display.set_icon(helpers.load_image('icon.png'))

        self._init_cards()
        self._start_new_game()

    def _start_new_game(self):
        """Start a new game."""
        logging.info('Initializing new game')

        self.tableau = [[] for _ in range(0, settings.TABLEAU_COLS)]

        self.deal(54)

    def _init_cards(self):
        self.cards = []

        for card_variant in settings.VARIANTS:
            for card_id in settings.CARDS.keys():
                self.cards.append(cards.Card(card_id, card_variant))

        random.shuffle(self.cards)

        return self.cards

    def deal(self, count):
        cards_per_columns = math.floor(count / settings.TABLEAU_COLS)

        cards_to_deal = [self.cards.pop(0) for _ in range(0, count)]

        for i in range(0, len(self.tableau)):
            self.tableau[i].extend(cards_to_deal[i:i + cards_per_columns])

    def update(self):
        """Perform every updates of the game logic, events handling and drawing.
        Also known as the game loop."""

        # Events handling
        for event in pygame.event.get():
            self._event_quit(event)

        # Drawings

        # TODO

        # PyGame-related updates
        pygame.display.update()

        self.clock.tick(settings.FPS)

    # --------------------------------------------------------------------------
    # Events handlers

    def _event_quit(self, event):
        """Called when the game must be closed."""
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    # --------------------------------------------------------------------------
    # Drawing handlers

    # TODO
