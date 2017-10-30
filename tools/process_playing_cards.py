from PIL import Image
from glob import glob
import logging
import click
import sys
import os


CARD_WIDTH = 100
CARDS_VARIANTS = ['spade', 'heart', 'diamond', 'club']


@click.command()
@click.option('--inputdir', '-i', help='Directory containing the cards PNG files')
@click.option('--outputdir', '-o', help='Root output directory')
def run(inputdir, outputdir):
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        stream=sys.stdout
    )

    logging.getLogger().setLevel(logging.INFO)

    context = click.get_current_context()

    if not inputdir or not outputdir:
        click.echo(run.get_help(context))
        context.exit()

    if not os.path.isdir(inputdir):
        raise FileNotFoundError(inputdir + ' does not exists')

    if not os.path.isdir(outputdir):
        raise FileNotFoundError(outputdir + ' does not exists')

    logging.info('Checking output sub-dirs')

    for card_variant in ['spade', 'heart', 'diamond', 'club']:
        card_variant_dir = os.path.join(outputdir, card_variant)

        if not os.path.isdir(card_variant_dir):
            logging.info('Creating output sub-dir ' + card_variant_dir)

            os.mkdir(card_variant_dir)

    logging.info('Preprocessing cards')

    card_paths = glob(os.path.join(inputdir, '*.png'))

    for card_path in list(card_paths):
        card_name = os.path.splitext(os.path.basename(card_path))[0]

        if card_name.endswith('joker'):
            card_paths.remove(card_path)
        elif card_name.endswith('2'):
            card_paths.remove(os.path.join(os.path.dirname(card_path), card_name.rstrip('2') + '.png'))

    logging.info('Processing cards')

    for card_path in card_paths:
        card_name = os.path.splitext(os.path.basename(card_path))[0]

        logging.info('Processing ' + card_name)

        card_type, card_variant = card_name.split('_of_')

        card_variant = card_variant.rstrip('s2')

        if card_variant not in CARDS_VARIANTS:
            logging.info(card_name + ': invalid variant "' + card_variant + '"')

            continue

        card_image = Image.open(card_path)
        card_image.thumbnail((CARD_WIDTH, CARD_WIDTH), Image.ANTIALIAS)
        card_image.save(os.path.join(outputdir, card_variant, card_type + '.png'), optimize=True)

if __name__ == '__main__':
    run()
