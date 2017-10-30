import settings
import helpers
import pygame


__all__ = [
    'Card'
]


class Card(pygame.sprite.Sprite):
    visible = False

    def __init__(self, id, variant):
        if id not in settings.CARDS:
            raise ValueError('Invalid card id provided')

        if variant not in settings.CARDS_VARIANTS:
            raise ValueError('Invalid card variant provided')

        super(Card, self).__init__()

        self.id = id
        self.power = settings.CARDS[id]
        self.variant = variant

        self.image = helpers.load_image('cards/' + self.variant + '/' + self.id + '.png')
        self.rect = self.image.get_rect()

    def __repr__(self):
        return '{}:{}'.format(self.id, self.variant)
