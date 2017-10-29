# Shell script to build the Spider Solitaire Mac OS executable.
# The resulting "spider_solitaire_mac.app" executable and "spider_solitaire_mac" script will be available in the "dist" directory.

pyinstaller \
    --clean --noconfirm --onefile --windowed \
    --log-level=WARN \
    --name="spider_solitaire_mac" \
    --icon="resources/images/icon.icns" \
    --add-data="resources:resources" \
    --osx-bundle-identifier="fr.epoc.python.games.spider_solitaire" \
    run.py