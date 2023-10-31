from .models import TraderData
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from pymongo import MongoClient

def user_dashboard(request):
    # Connect to your MongoDB using the configured settings
    client = MongoClient()
    db = client['trader_dashboard_db']
    collection = db['trader_data']

    # Retrieve data for the user (you may need to filter by user ID)
    trader_data = collection.find({'trader_id': request.user.id})

    # Prepare data for the graph (timestamps and balances)
    timestamps = [entry['timestamp'] for entry in trader_data]
    balances = [entry['balance'] for entry in trader_data]

    return render(request, 'user_dashboard.html', {
        'timestamps': timestamps,
        'balances': balances,
    })



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user-dashboard/')  # Redirect to the user dashboard after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_dashboard') 


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')  # Redirect to the user dashboard after login
    return render(request, 'registration/login.html')


def admin_dashboard(request):
    # Connect to your MongoDB using the configured settings
    client = MongoClient()
    db = client['your-database-name']
    collection = db['trader_data']

    # Retrieve all trader data
    trader_data = collection.find()

    return render(request, 'admin_dashboard.html', {
        'trader_data': trader_data,
    })