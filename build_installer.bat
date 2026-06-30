@echo off
setlocal

if not exist "dist\FlappyBird.exe" (
  echo FlappyBird.exe introuvable dans dist\.
  echo Lance d abord build_windows.bat.
  exit /b 1
)

set "ISCC_PATH="

if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
  set "ISCC_PATH=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
)

if not defined ISCC_PATH (
  for /f "delims=" %%I in ('where ISCC.exe 2^>nul') do (
    set "ISCC_PATH=%%I"
    goto :found_iscc
  )
)

:found_iscc
if not defined ISCC_PATH (
  echo Inno Setup n est pas installe ou ISCC.exe n est pas accessible.
  echo Installe Inno Setup puis relance ce script.
  exit /b 1
)

"%ISCC_PATH%" flappy_bird_installer.iss

endlocal
