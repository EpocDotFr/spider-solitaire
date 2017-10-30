import settings


__all__ = [
    'Card'
]


class Card:
    visible = False

    def __init__(self, id, variant):
        if id not in settings.CARDS:
            raise ValueError('Invalid card id provided')

        if variant not in settings.CARDS_VARIANTS:
            raise ValueError('Invalid card variant provided')

        self.id = id
        self.power = settings.CARDS[id]
        self.variant = variant

    def __repr__(self):
        return '{}:{}'.format(self.id, self.variant)
