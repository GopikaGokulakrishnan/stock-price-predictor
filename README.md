# 📈 AI Stock Price Predictor

A sophisticated web application that uses LSTM neural networks to predict stock prices with a beautiful, responsive interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🤖 AI-powered stock price predictions using LSTM neural networks
- 📈 Real-time data from Yahoo Finance API
- 🎨 Beautiful, responsive UI with interactive charts
- 📊 Technical indicators (RSI, MACD, Moving Averages)
- 🔮 Multi-timeframe predictions (1 week to 3 months)
- 📱 Mobile-friendly design

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/stock-price-predictor.git
cd stock-price-predictor

# Create virtual environment
python -m venv stock_env
stock_env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Visit http://localhost:5000



🛠️ Tech Stack
Backend: Python, Flask, TensorFlow, yFinance, Pandas, NumPy
Frontend: HTML5, CSS3, JavaScript, Bootstrap 5, Plotly.js
ML: LSTM Neural Networks, Technical Analysis


📁 Project Structure

stock-price-predictor/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── models/               # ML models
│   ├── lstm_model.py     # LSTM neural network
│   └── model_utils.py    # Model utilities
├── data/                 # Data handling
│   └── data_loader.py    # Data preprocessing
├── static/               # Frontend assets
└── templates/            # HTML templates
    └── index.html

    ⚠️ Disclaimer

    This project is for educational purposes only. Not financial advice.

    📄 License
MIT License - see LICENSE file for details.


### 2. Create `LICENSE` file:

```text
MIT License

Copyright (c) 2024 YOUR_NAME

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
