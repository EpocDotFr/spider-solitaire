@ECHO off
REM Batch script to build the Spider Solitaire Windows executable.
REM The resulting "spider_solitaire_windows.exe" executable will be available in the "dist" directory.

pyinstaller ^
    --clean --noconfirm --onefile --windowed ^
    --log-level=WARN ^
    --name="spider_solitaire_windows" ^
    --icon="resources/images/icon.ico" ^
    --add-data="resources;resources" ^
    run.py