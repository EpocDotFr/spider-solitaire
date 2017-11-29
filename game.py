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

        # TODO Load the others images here one time and assign them to the cards later

    def _load_random_music(self):
        """Load and play a random music."""
        logging.info('Loading random music')

        helpers.load_random_music(['cryptic_puzzler2.wav', 'piano_puzzles.wav'], volume=settings.MUSIC_VOLUME)

    def _start_new_game(self):
        """Start a new game."""
        logging.info('Initializing new game')

        self.available_cards = cards.get_cards(2)
        self.complete_stacks = []

        random.shuffle(self.available_cards)

        self.tableau = [[] for _ in range(0, settings.PILES)]

        self.selected_cards = []

        self._load_random_music()

        self._deal(settings.CARDS_INITIAL_DEAL)

    def _can_deal(self):
        """Check if there's at least one card per pile except if there's not enough cards in the tableau."""
        total_per_piles = [len(pile) for pile in self.tableau]
        tableau_total = sum(total_per_piles)

        # There isn't enough cards for each piles
        if tableau_total < settings.PILES:
            return True

        # Check each piles for one that is empty
        for pile_total in total_per_piles:
            if pile_total == 0:
                return False

        return True

    def _deal(self, count):
        """Deal a specified amount of cards, distributed in each piles of the tableau."""
        if not self._can_deal():
            logging.info('Cannot deal: empty piles exists')

            return False

        logging.info('Dealing {} cards'.format(count))

        cards_per_piles = math.floor(count / settings.PILES)

        for i in range(0, settings.PILES):
            for j in range(0, cards_per_piles):
                card = self.available_cards.pop(0)

                if j == cards_per_piles - 1:
                    card.is_face_down = False
                else:
                    card.is_face_down = True

                self.tableau[i].append(card)

        self._update_available_cards()

        return True

    def _update_available_cards(self):
        """Update the cards objects of the available cards."""
        self.available_cards_images = []

        cards_to_draw = len(list(range(0, len(self.available_cards), settings.CARDS_PER_DEAL))) - 1

        for i in range(0, cards_to_draw):
            self.available_cards_images.append(cards.FaceDownCard())

    def _handle_complete_stacks(self):
        """Check each piles for complete stacks."""
        for pile in self.tableau:
            complete_stack_cards = []

            for i, card in enumerate(pile): # For each cards in each piles
                if card.is_face_down: # The card isn't visible: ignore
                    continue

                if i == len(pile) - 1: # The card is the last one of the pile: end handling this pile
                    break

                upper_card = pile[i + 1]

                if card.is_direct_previous(upper_card):
                    complete_stack_cards.append(card)

            # If there's one complete stack, pull all of these cards into the complete stacks deck
            if len(complete_stack_cards) == len(cards.CARDS):
                for card in complete_stack_cards:
                    self.complete_stacks.append(card)
                    pile.remove(card)

    def update(self):
        """Perform every updates of the game logic, events handling and drawing.
        Also known as the game loop."""

        # Events handling
        for event in pygame.event.get():
            event_handlers = [
                self._event_quit,
                self._event_deal,
                self._event_select_tableau_cards,
                self._event_place_tableau_cards
            ]

            for handler in event_handlers:
                if handler(event):
                    break

        # Drawings
        self._draw_background()
        self._draw_available_cards()
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

        return False

    def _event_deal(self, event):
        """Deal cards if the player clicked on any of the vailable cards deck."""
        if self._was_an_available_card_clicked(event):
            self._deal(settings.CARDS_PER_DEAL)
            self._handle_complete_stacks()

            return True

        return False

    def _event_select_tableau_cards(self, event):
        """Select one or more cards from the tableau."""
        card = self._get_clicked_tableau_card(event)

        if not card:
            return False

        logging.info('{} was clicked'.format(card))

        self.selected_cards.append(card) # TODO

        return True

    def _event_place_tableau_cards(self, event):
        """Place one or more cards on the tableau."""
        pile = self._get_clicked_pile(event)

        if not pile:
            return False

        for card in self.selected_cards:
            self.tableau[pile].append(card)
            self.selected_cards.remove(card)

        return True

    def _was_an_available_card_clicked(self, event):
        """Click on any of the available cards deck."""
        if event.type == pygame.MOUSEBUTTONUP:
            for card in self.available_cards_images:
                if card.rect.collidepoint(event.pos):
                    return True

        return False

    def _get_clicked_tableau_card(self, event):
        """Get the card that was clicked on the tableau."""
        if event.type == pygame.MOUSEBUTTONUP and not self.selected_cards:
            for pile in self.tableau:
                for card in reversed(pile):
                    if card.rect.collidepoint(event.pos):
                        return card

        return False

    def _get_clicked_pile(self, event):
        """Return the pile ID in which a card was clicked on."""
        if event.type == pygame.MOUSEBUTTONUP and self.selected_cards:
            for i, pile in enumerate(self.tableau):
                for card in reversed(pile):
                    if card.rect.collidepoint(event.pos):
                        return i

        return False

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

    def _draw_available_cards(self):
        """Draw the available cards deck. One face down card per 10 available cards."""
        for i, card in enumerate(self.available_cards_images):
            card.rect.top = settings.WINDOW_PADDING
            card.rect.right = self.window_rect.w - (settings.WINDOW_PADDING + (i * ((settings.CARDS_WIDTH * 25) / 100)))

            self.window.blit(card.image, card.rect)

    def _draw_tableau(self):
        """Draw the tableau."""
        for pile_num, pile_cards in enumerate(self.tableau):
            pile_top = settings.TABLEAU_TOP
            pile_left = pile_num * settings.CARDS_WIDTH + pile_num * settings.CARDS_HORIZONTAL_MARGIN + settings.WINDOW_PADDING

            for pile_card_num, pile_card in enumerate(pile_cards):
                pile_card.rect.top = pile_top
                pile_card.rect.left = pile_left

                margin_factor = 10 if pile_card.is_face_down else 30

                pile_top += (settings.CARDS_HEIGHT * margin_factor) / 100

                self.window.blit(pile_card.image, pile_card.rect)
