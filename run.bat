@echo off
cd /d "%~dp0"
call stock_env\Scripts\activate.bat
python run.py
pause