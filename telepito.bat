@echo off
setlocal EnableDelayedExpansion
chcp 65001 > nul

echo [1/5] Venv létrehozása...
python -m venv venv

echo [2/5] Venv aktiválása...
call venv\Scripts\activate.bat

echo [3/5] pip frissítése...
python -m pip install --upgrade pip

echo [4/5] Követelmények telepítése...
pip install -r my_final_project\requirements.txt

echo [5/5] Projekt indítása...

echo ---
echo ✅ Kész! A környezet aktív és a projekt fut.
pause

cls
python my_final_project\indito.py
