import os
from datetime import datetime, timedelta

class Config:
    # Model parameters
    SEQUENCE_LENGTH = 60
    TRAIN_TEST_SPLIT = 0.8
    EPOCHS = 50
    BATCH_SIZE = 32
    
    # Data parameters
    DEFAULT_START_DATE = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
    DEFAULT_END_DATE = datetime.now().strftime('%Y-%m-%d')
    
    # Available stocks
    AVAILABLE_STOCKS = {
        'AAPL': 'Apple Inc.',
        'GOOGL': 'Alphabet Inc.',
        'MSFT': 'Microsoft Corporation',
        'AMZN': 'Amazon.com Inc.',
        'TSLA': 'Tesla Inc.',
        'META': 'Meta Platforms Inc.',
        'NFLX': 'Netflix Inc.',
        'NVDA': 'NVIDIA Corporation',
        'JPM': 'JPMorgan Chase & Co.',
        'JNJ': 'Johnson & Johnson'
    }