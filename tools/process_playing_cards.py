# This script takes all the cards images from the Kenney's boardgame pack (http://kenney.nl/assets/boardgame-pack),
# resize them and saves them in ../resources/images/cards directory

from PIL import Image
from glob import glob
import logging
import click
import sys
import os
import re


CARDS_WIDTH = 70
CARDS_VARIANTS = ['spades', 'hearts', 'diamonds', 'clubs']

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z0-9])')


def snake_case(string):
    s1 = first_cap_re.sub(r'\1_\2', string)

    return all_cap_re.sub(r'\1_\2', s1).lower()


@click.command()
@click.option('--inputdir', '-i', help='Directory containing the cards PNG files')
def run(inputdir):
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        stream=sys.stdout
    )

    logging.getLogger().setLevel(logging.INFO)

    context = click.get_current_context()

    if not inputdir:
        click.echo(run.get_help(context))
        context.exit()

    if not os.path.isdir(inputdir):
        raise FileNotFoundError(inputdir + ' does not exists')

    outputdir = os.path.realpath('../resources/images/cards')

    logging.info('Checking output sub-dirs')

    for card_variant in CARDS_VARIANTS:
        card_variant_dir = os.path.join(outputdir, card_variant)

        if not os.path.isdir(card_variant_dir):
            logging.info('Creating output sub-dir ' + card_variant_dir)

            os.mkdir(card_variant_dir)

    card_paths = glob(os.path.join(inputdir, '*.png'))

    logging.info('Processing cards')

    for card_path in card_paths:
        card_name = os.path.splitext(os.path.basename(card_path))[0]

        if card_name.startswith('cardBack') or card_name == 'cardJoker':
            logging.info('Ignoring ' + card_name)

            continue

        logging.info('Processing ' + card_name)

        card_name = snake_case(card_name.replace('card', ''))

        card_variant, card_type = card_name.split('_')

        if card_variant not in CARDS_VARIANTS:
            logging.info(card_name + ': invalid variant "' + card_variant + '"')

            continue

        if card_type == 'a':
            card_type = 'ace'
        elif card_type == 'j':
            card_type = 'jack'
        elif card_type == 'k':
            card_type = 'king'
        elif card_type == 'q':
            card_type = 'queen'

        card_image = Image.open(card_path)
        card_image.thumbnail((CARDS_WIDTH, 9999), Image.ANTIALIAS)
        card_image.save(os.path.join(outputdir, card_variant, card_type + '.png'), optimize=True)

if __name__ == '__main__':
    run()
