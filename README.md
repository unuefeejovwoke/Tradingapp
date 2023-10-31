# Tradingapp
Our startup has given 10 stock traders $100 each to trade. The Dynamic User and Admin Dashboard App is designed to allow each trader to track their profit or loss over time, with data points recorded at 1-minute intervals. Additionally, an admin dashboard provides a way for managers to track the performance of the 10 traders.


# Dynamic User and Admin Dashboard App

## Overview

The Dynamic User and Admin Dashboard App is a Django-based project designed to allow 10 stock traders to track their profit and loss over time at 1-minute intervals. Additionally, an admin dashboard provides performance tracking for the 10 traders.

## Features

- Simulate profit and loss data for 10 traders.
- Store trading data in a MongoDB database.
- Create a user dashboard with a graph displaying profit or loss over time.
- Create an admin dashboard for performance tracking.


## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- Django
- MongoDB
- Additional Python packages (See `requirements.txt`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/unuefeejovwoke/tradingapp.git

python -m venv venv

source venv/bin/activate  # On Windows, use venv\Scripts\activate


pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Access the user dashboard at http://localhost:8000/user-dashboard/.

Access the admin dashboard at http://localhost:8000/admin-dashboard/.

Running the Simulation Script
To simulate trading data, run the following command:

python manage.py simulate_trading_data
User Dashboard
Users can access the user dashboard to view their trading data and the graph displaying profit or loss over time.

Admin Dashboard
Admins can access the admin dashboard to track the performance of the 10 traders.

Contributing
We welcome contributions to this project. To contribute, follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.

