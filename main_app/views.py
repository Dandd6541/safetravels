from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Trip
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Add the following import

# Create your views here
# Define the home view
class TripCreate(CreateView):
  model = Trip
  fields = ['name', 'city', 'county', 'stayLength', 'date', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', { 'trips': trips})
  
def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  return render(request, 'trips/detail.html', { 'trip': trip })



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
