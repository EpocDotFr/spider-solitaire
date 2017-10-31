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
        self._start_new_game()

    def _load_images(self):
        """Load all images."""
        logging.info('Loading images')

        self.images = {}
        self.images['background'] = helpers.load_image('background.png')

    def _start_new_game(self):
        """Start a new game."""
        logging.info('Initializing new game')

        self._init_deck()

        self.tableau = [[] for _ in range(0, settings.PILES)]

        self._deal(settings.CARDS_INITIAL_DEAL)

    def _init_deck(self):
        """Initialize the deck (cards instances): all the 52 cards * 2."""
        logging.info('Initializing deck')

        self.deck = cards.get_cards(2)

        random.shuffle(self.deck)

    def _deal(self, count):
        """Deal a specified amount of cards in the piles of the tableau."""
        logging.info('Dealing {} cards'.format(count))

        cards_per_piles = math.floor(count / settings.PILES)

        for i in range(0, settings.PILES):
            for _ in range(0, cards_per_piles):
                self.tableau[i].append(self.deck.pop(0))

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

        y_count = math.ceil(self.window_rect.h / bg_height)
        x_count = math.ceil(self.window_rect.w / bg_width)

        for y in range(0, y_count):
            for x in range(0, x_count):
                bg_rect = self.images['background'].get_rect()
                bg_rect.left += x * bg_width
                bg_rect.top += y * bg_height

                self.window.blit(self.images['background'], bg_rect)

    def _draw_deck(self):
        """Draw the deck. One face down card per 10 cards."""
        cards_to_draw = len(list(range(0, len(self.deck), settings.CARDS_PER_DEAL))) - 1

        for i in range(0, cards_to_draw):
            face_down_card = cards.FaceDownCard()
            face_down_card.rect.top = settings.WINDOW_PADDING
            face_down_card.rect.right = self.window_rect.w - (settings.WINDOW_PADDING + ((i * settings.CARDS_WIDTH) / 4))

            self.window.blit(face_down_card.image, face_down_card.rect)

    def _draw_tableau(self):
        """Draw the tableau."""
        for pile_num, pile_cards in enumerate(self.tableau):
            pile_cards_count = len(pile_cards)

            for pile_card_num, pile_card in enumerate(pile_cards):
                if pile_card_num == pile_cards_count - 1:
                    pile_card.set_face_down(False)
                else:
                    pile_card.set_face_down(True)

                pile_card.rect.top = settings.TABLEAU_TOP + ((pile_card_num * settings.CARDS_HEIGHT) / 3)
                pile_card.rect.left = pile_num * settings.CARDS_WIDTH + pile_num * settings.CARDS_HORIZONTAL_MARGIN + settings.WINDOW_PADDING

                self.window.blit(pile_card.image, pile_card.rect)
