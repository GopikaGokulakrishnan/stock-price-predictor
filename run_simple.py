import os
import sys
import webbrowser
from threading import Timer
from app import app

def open_browser():
    """Open browser after 2 seconds when server starts"""
    Timer(2, lambda: webbrowser.open('http://localhost:5000')).start()

if __name__ == '__main__':
    print("🎯 Starting Simple Stock Predictor...")
    print("🌐 Server will start at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop")
    print("\n" + "="*50)
    
    # Open browser automatically
    open_browser()
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)