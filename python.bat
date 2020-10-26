@echo off

echo.
echo patching python..

timeout /t 3 /nobreak > NUL


echo.
echo.

py -m pip install --upgrade pip
py -m pip install pillow
py -m pip install pyautogui
py -m pip install opencv-python
py -m pip install psutil
py -m pip install colorama
py -m pip install winshell
py -m pip install pypiwin32


timeout /t 3 /nobreak > NUL
echo.
echo.
echo done





pause