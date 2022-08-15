from django.shortcuts import render
from .models import Trip
# Add the following import

# Create your views here
# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', { 'trips': trips})