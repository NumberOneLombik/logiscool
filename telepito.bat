@echo off

set myPath=%CD% 
::%~dp0

echo [1/3] Venv létrehozása...
python -m venv venv

echo [2/3] Venv aktiválása...
call venv\Scripts\activate.bat

echo [3/3] Könyvtárak telepítése...
pip install -r %myPath%/requirements.txt

echo Kész! A venv aktív.

pause
cls

python ./my_final_project/indito.py
