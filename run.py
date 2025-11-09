#!/usr/bin/env python3
"""
Stock Price Predictor - Main Application Runner
"""

import os
import sys
from app import app

def main():
    """Main application entry point"""
    print("🚀 Starting AI Stock Price Predictor...")
    print("📊 Developed with Python, TensorFlow, and Flask")
    print("🌐 Access the application at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        # Run the Flask application
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down Stock Price Predictor...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()