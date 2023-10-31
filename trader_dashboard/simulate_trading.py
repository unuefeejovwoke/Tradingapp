# simulate_trading_data.py
import os
import random
from datetime import datetime, timedelta
import django
from django.conf import settings
from pymongo import MongoClient

# Set the DJANGO_SETTINGS_MODULE and initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trader_dashboard.settings")
django.setup()

# Connect to your MongoDB using the Django settings
client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client[settings.DATABASES['default']['NAME']]
collection = db['trader_data']

# Simulate trading data for 10 traders
traders = 10
initial_balance = 100

for i in range(traders):
    trader_data = []
    balance = initial_balance
    timestamp = datetime.now()

    for _ in range(1440):  # Simulate data for 24 hours (1 data point per minute)
        # Simulate profit or loss
        profit_loss = random.uniform(-2, 2)
        balance += profit_loss

        # Store data point in MongoDB
        data_point = {
            'timestamp': timestamp,
            'balance': balance,
            'trader_id': i + 1,  # Trader IDs start from 1
        }
        collection.insert_one(data_point)

        # Update timestamp for the next minute
        timestamp += timedelta(minutes=1)
