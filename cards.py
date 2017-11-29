import helpers
import pygame


__all__ = [
    'Card'
]

CARDS = {
    'king': 1,
    'queen': 2,
    'jack': 3,
    '10': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
    'ace': 13
}

CARDS_VARIANTS = ['spades', 'hearts', 'diamonds', 'clubs']


class Card(pygame.sprite.Sprite):
    _is_face_down = False

    def __init__(self, id, variant):
        super(Card, self).__init__()

        if id not in CARDS:
            raise ValueError('Invalid card id provided')

        if variant not in CARDS_VARIANTS:
            raise ValueError('Invalid card variant provided')

        self.id = id
        self.power = CARDS[id]
        self.variant = variant

    @property
    def is_face_down(self):
        return self._is_face_down

    @is_face_down.setter
    def is_face_down(self, value):
        self._is_face_down = value

        if self._is_face_down:
            self.image = helpers.load_image('cards/back.png')
        else:
            self.image = helpers.load_image('cards/' + self.variant + '/' + self.id + '.png')

        self.rect = self.image.get_rect()

    def is_direct_next(self, other):
        return self.power + 1 == other.power

    def is_direct_previous(self, other):
        return self.power - 1 == other.power

    def __repr__(self):
        return 'Card:{}:{}'.format(self.id, self.variant)


class FaceDownCard(pygame.sprite.Sprite):
    def __init__(self):
        super(FaceDownCard, self).__init__()

        self.image = helpers.load_image('cards/back.png')
        self.rect = self.image.get_rect()

    def __repr__(self):
        return 'FaceDownCard'


def get_cards(nb_times=1):
    """Instanciate a Card instance for each cards combination, up to nb_times each."""
    ret = []

    for _ in range(0, nb_times):
        for card_variant in CARDS_VARIANTS:
            for card_id in CARDS.keys():
                ret.append(Card(card_id, card_variant))

    return ret
