# Spider Solitaire

The [Spider Solitaire](https://en.wikipedia.org/wiki/Spider_(solitaire)) cards game, implemented in Python.

> TODO Screenshot

## Features

> TODO

## Prerequisites

Python 3. May eventually works with Python 2 (not tested).

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Usage

```
python run.py
```

### Controls

> TODO

### Process playing cards

> TODO

## How it works

This game is built on top of [PyGame](http://www.pygame.org/hifi.html). I obviously can't explain how it
works here, so you'll have to jump yourself in the source code. Start with the entry point, `run.py`.

Beside the game itself, I use [PyInstaller](http://www.pyinstaller.org/) to generate the executables. It packs
up all the game and its assets in a single executable file so players just have to run it with nothing to install.
This task is performed by the `build_*` scripts to be run in the corresponding OS.

## Credits

  - Icon by [Everaldo Coelho](https://www.iconfinder.com/icons/4219/card_game_poker_icon) (freeware)
  - Playing cards by [Kenney](http://kenney.nl/assets/boardgame-pack) (CC0 1.0 Universal)
  - Background by [Subtle Patterns](https://www.toptal.com/designers/subtlepatterns/pool-table/) (CC BY-SA 3.0)
  - Sound effects by [Kenney](https://kenney.nl/assets/casino-audio) (CC0 1.0 Universal)
  - Musics by [SoundImage.org](http://soundimage.org/) (Royalty-Free)

## End words

If you have questions or problems, you can [submit an issue](https://github.com/EpocDotFr/spider-solitaire/issues).

You can also submit pull requests. It's open-source man!