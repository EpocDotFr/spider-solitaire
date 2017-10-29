# Shell script to build the Spider Solitaire Linux executable.
# The resulting "spider_solitaire_linux" script will be available in the "dist" directory.

pyinstaller \
    --clean --noconfirm --onefile \
    --log-level=WARN \
    --name="spider_solitaire_linux" \
    --add-data="resources:resources" \
    run.py