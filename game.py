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

        self._load_images()
        self._init_cards()
        self._start_new_game()

    def _load_images(self):
        """Load all the images resources."""
        logging.info('Loading images')

        self.images = {}
        self.images['background'] = helpers.load_image('background.png')

    def _init_cards(self):
        """Initialize the cards instances (all the 52 cards * 2)."""
        self.deck = cards.get_cards(2)

        random.shuffle(self.deck)

    def _start_new_game(self):
        """Start a new game."""
        logging.info('Initializing new game')

        self.tableau = [[] for _ in range(0, settings.PILES)]

        self._deal(54)

    def _deal(self, count):
        """Deal count cards to the tableau."""
        cards_per_piles = math.floor(count / settings.PILES)

        cards_to_deal = [self.deck.pop(0) for _ in range(0, count)]

        for i in range(0, len(self.tableau)):
            self.tableau[i].extend(cards_to_deal[i:i + cards_per_piles])

    def update(self):
        """Perform every updates of the game logic, events handling and drawing.
        Also known as the game loop."""

        # Events handling
        for event in pygame.event.get():
            self._event_quit(event)

        # Drawings
        self._draw_background()
        self._draw_deck()
        self._draw_tableau()

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

    def _draw_background(self):
        """Draw the game background."""
        bg_width, bg_height = self.images['background'].get_size()

        y_count = math.ceil(self.window.get_height() / bg_height)
        x_count = math.ceil(self.window.get_width() / bg_width)

        for y in range(0, y_count):
            for x in range(0, x_count):
                bg_rect = self.images['background'].get_rect()
                bg_rect.left += x * bg_width
                bg_rect.top += y * bg_height

                self.window.blit(self.images['background'], bg_rect)

    def _draw_deck(self):
        pass # TODO

    def _draw_tableau(self):
        for pile_num, pile_cards in enumerate(self.tableau):
            pile_cards[0].rect.top = settings.WINDOW_PADDING + settings.CARDS_HEIGHT + settings.CARDS_VERTICAL_MARGIN
            pile_cards[0].rect.left = pile_num * pile_cards[0].rect.w + pile_num * settings.CARDS_HORIZONTAL_MARGIN + settings.WINDOW_PADDING

            self.window.blit(pile_cards[0].image, pile_cards[0].rect)
