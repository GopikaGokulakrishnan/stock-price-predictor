@echo off
echo Installing required packages...
python -m pip install --upgrade pip
pip install flask yfinance numpy
echo.
echo ✅ Installation complete!
echo.
echo Now run: python run_simple.py
pause