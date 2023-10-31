# data_generation_script.py
import random
import time
from tradeapp.models import TraderData  # Make sure to import the TraderData model

while True:
    profit_loss = round(random.uniform(-5, 5), 2)  # Generate a random profit/loss value
    TraderData.objects.create(profit_loss=profit_loss)  # Store this value in your MongoDB database
    time.sleep(60)  # Wait for 1 minute before the next update
