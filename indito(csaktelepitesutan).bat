@echo off
set bathelye=%~dp0

echo Projektinditas...

call %bathelye%venv\Scripts\activate.bat
echo Venv aktiválva.
echo ---
echo Kész! A környezet aktív és a projekt fut.
pause
cls
python %bathelye%my_final_project\indito.py
pause