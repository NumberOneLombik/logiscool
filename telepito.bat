@echo off
setlocal EnableDelayedExpansion
chcp 65001 > nul

echo Venv letrehozasa...
python -m venv venv

echo Venv aktivalasa...
call venv\Scripts\activate.bat

echo pip frissitese...
python -m pip install --upgrade pip

echo Kovetelmenyek telepitese...
pip install -r my_final_project\requirements.txt

echo Projekt inditasa...

echo ---
echo Kesz! A kornyezet aktiv és a projekt fut.
pause

cls
python my_final_project\indito.py
