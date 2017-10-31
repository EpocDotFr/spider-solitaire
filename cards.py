import helpers
import pygame


__all__ = [
    'Card'
]

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


class Card(pygame.sprite.Sprite):
    def __init__(self, id, variant, visible=False):
        super(Card, self).__init__()

        if id not in CARDS:
            raise ValueError('Invalid card id provided')

        if variant not in CARDS_VARIANTS:
            raise ValueError('Invalid card variant provided')

        self.id = id
        self.power = CARDS[id]
        self.variant = variant

        self.set_visible(visible)

    def set_visible(self, is_visible):
        self.is_visible = is_visible

        if self.is_visible:
            self.image = helpers.load_image('cards/' + self.variant + '/' + self.id + '.png')
        else:
            self.image = helpers.load_image('cards/back.png')

        self.rect = self.image.get_rect()

    def __repr__(self):
        return '{}:{}'.format(self.id, self.variant)


def get_cards(nb_times=1):
    """Instanciate a Card instance for each cards combination, up to nb_times each."""
    ret = []

    for _ in range(0, nb_times):
        for card_variant in CARDS_VARIANTS:
            for card_id in CARDS.keys():
                ret.append(Card(card_id, card_variant))

    return ret
