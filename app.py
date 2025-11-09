from flask import Flask, render_template, request, jsonify
import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Available stocks
AVAILABLE_STOCKS = {
    'AAPL': 'Apple Inc.',
    'GOOGL': 'Alphabet Inc. (Google)',
    'MSFT': 'Microsoft Corporation',
    'AMZN': 'Amazon.com Inc.',
    'TSLA': 'Tesla Inc.',
    'META': 'Meta Platforms Inc.',
    'NVDA': 'NVIDIA Corporation',
    'NFLX': 'Netflix Inc.'
}

class StockPredictor:
    def __init__(self):
        pass
    
    def get_stock_data(self, symbol, period='6mo'):
        """Get stock data from Yahoo Finance"""
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period=period)
            return hist
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def calculate_prediction(self, symbol, days=30):
        """Calculate stock price prediction"""
        try:
            # Get historical data
            hist = self.get_stock_data(symbol, '1y')
            
            if hist.empty or len(hist) < 30:
                raise ValueError("Not enough historical data")
            
            current_price = hist['Close'].iloc[-1]
            
            # Use multiple methods for better prediction
            recent_prices = hist['Close'].tail(60).values
            
            # Method 1: Linear regression trend
            x = np.arange(len(recent_prices))
            slope, intercept = np.polyfit(x, recent_prices, 1)
            trend_prediction = current_price + (slope * days)
            
            # Method 2: Moving average momentum
            short_ma = np.mean(recent_prices[-10:])  # 10-day MA
            long_ma = np.mean(recent_prices[-30:])   # 30-day MA
            momentum = (short_ma - long_ma) / long_ma
            momentum_prediction = current_price * (1 + momentum * days/10)
            
            # Method 3: Volatility-adjusted prediction
            volatility = np.std(recent_prices[-20:]) / np.mean(recent_prices[-20:])
            volatility_factor = 1 + (volatility * 0.5)
            
            # Combine predictions (weighted average)
            predicted_price = (trend_prediction * 0.4 + 
                             momentum_prediction * 0.4 + 
                             current_price * volatility_factor * 0.2)
            
            # Ensure reasonable bounds
            max_change = 0.3  # 30% max change
            predicted_price = max(predicted_price, current_price * (1 - max_change))
            predicted_price = min(predicted_price, current_price * (1 + max_change))
            
            # Calculate confidence based on data quality and volatility
            confidence = max(60, 90 - (volatility * 100))
            
            return {
                'current_price': round(current_price, 2),
                'predicted_price': round(predicted_price, 2),
                'change_percent': round(((predicted_price - current_price) / current_price) * 100, 2),
                'confidence': round(confidence),
                'volatility': round(volatility * 100, 2)
            }
            
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html', stocks=AVAILABLE_STOCKS)

@app.route('/get_stock_info', methods=['POST'])
def get_stock_info():
    """Get current stock information"""
    try:
        symbol = request.json['symbol']
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period='1d')
        
        stock_info = {
            'name': info.get('longName', symbol),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'currentPrice': round(hist['Close'].iloc[-1], 2) if not hist.empty else 'N/A',
            'marketCap': f"${info.get('marketCap', 0)/1e9:.2f}B" if info.get('marketCap') else 'N/A',
            'peRatio': round(info.get('trailingPE', 0), 2) if info.get('trailingPE') else 'N/A',
            'volume': f"{info.get('volume', 0):,}" if info.get('volume') else 'N/A',
            'fiftyTwoWeekHigh': round(info.get('fiftyTwoWeekHigh', 0), 2) if info.get('fiftyTwoWeekHigh') else 'N/A',
            'fiftyTwoWeekLow': round(info.get('fiftyTwoWeekLow', 0), 2) if info.get('fiftyTwoWeekLow') else 'N/A'
        }
        
        return jsonify({'status': 'success', 'info': stock_info})
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    """Generate stock price prediction"""
    try:
        symbol = request.json['symbol']
        days = int(request.json.get('days', 30))
        
        if days < 7 or days > 90:
            return jsonify({'status': 'error', 'message': 'Prediction days must be between 7 and 90'})
        
        predictor = StockPredictor()
        prediction = predictor.calculate_prediction(symbol, days)
        
        # Get historical data for chart
        hist_data = predictor.get_stock_data(symbol, '6mo')
        dates = hist_data.index.strftime('%Y-%m-%d').tolist()
        prices = hist_data['Close'].tolist()
        
        return jsonify({
            'status': 'success',
            'symbol': symbol,
            'prediction': prediction,
            'historical_data': {
                'dates': dates,
                'prices': prices
            }
        })
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/test')
def test():
    return "✅ Flask server is working correctly!"

if __name__ == '__main__':
    print("🚀 Starting AI Stock Price Predictor...")
    print("📊 Available stocks:", list(AVAILABLE_STOCKS.keys()))
    print("🌐 Server will be available at: http://localhost:5000")
    print("🔍 Test the server at: http://localhost:5000/test")
    print("⏹️  Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)