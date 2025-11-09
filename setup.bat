@echo off
echo Starting Stock Predictor Setup...
echo.

:: Change to this directory
cd /d "%~dp0"

:: Create virtual environment
echo Creating virtual environment...
python -m venv stock_env

:: Activate and install packages
echo Installing dependencies...
call stock_env\Scripts\activate.bat
pip install --upgrade pip
pip install flask==2.3.3 pandas==2.0.3 numpy==1.24.3 scikit-learn==1.3.0 yfinance==0.2.18 plotly==5.15.0 requests==2.31.0 python-dotenv==1.0.0

:: Create directories
echo Creating folders...
mkdir data 2>nul
mkdir data\historical_data 2>nul
mkdir static 2>nul
mkdir static\css 2>nul
mkdir static\js 2>nul
mkdir static\images 2>nul
mkdir templates 2>nul
mkdir models 2>nul

echo.
echo ✅ Setup complete!
echo.
echo To run the application:
echo 1. Double-click run.bat
echo 2. OR Open cmd and run:
echo    C:\StockPredictor\stock_env\Scripts\activate.bat
echo    python run.py
echo.
pause