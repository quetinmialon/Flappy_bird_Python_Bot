@echo off
setlocal

pyinstaller ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --name FlappyBird ^
  --add-data "bird.png;." ^
  --add-data "pipe.png;." ^
  play.py

endlocal
