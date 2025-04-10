@echo off
set bathelye=%~dp0

echo Venv letrehozasa...
python -m venv venv

echo Venv aktivalasa...
call %bathelye%venv\Scripts\activate.bat

echo pip frissitese...
python -m pip install --upgrade pip

echo Kovetelmenyek telepitese...
pip install -r %bathelye%my_final_project\requirements.txt
pip install -e %bathelye%my_final_project\my_first_package

echo Projekt inditasa...

echo ---
echo Kesz! A kornyezet aktiv es a projekt fut, mihelyt elinditod/ja az indito(csaktelepitesutan).bat-ot.
pause
cls