from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from .models import Trip, People 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Imports login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# Add the following import
import requests

# Create your views here
# Define the home view
class TripCreate(LoginRequiredMixin, CreateView):
  model = Trip
  fields = ['name', 'city', 'cityFrom','county', 'stayLength', 'date', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = ['name', 'city', 'cityFrom', 'county', 'stayLength', 'date', 'description']

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/trips/'


@login_required
def assoc_people(request, trip_id, people_id):
  trip = Trip.objects.get(id=trip_id)
  trip.peoples.add(people_id)
  return redirect('detail', trip_id=trip_id)

@login_required
def unassoc_people(request, trip_id, people_id):
  Trip.objects.get(id=trip_id).peoples.remove(people_id)
  return redirect('detail', trip_id=trip_id)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def covid(request):
    return render(request, 'covid.html')

def covid_query(request):
    print(request.POST.get('state'))
    state = request.POST.get('state')
    c = requests.get(f'https://disease.sh/v3/covid-19/historical/usacounties/{state}?lastdays=7')
    c = c.json()
    print(c)
    return render(request, 'covidquery.html', {'c': c})

@login_required
def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', { 'trips': trips})

@login_required  
def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  id_list = trip.peoples.all().values_list('id')
  peoples_trip_doesnt_have = People.objects.exclude(id__in=id_list)
  return render(request, 'trips/detail.html', {
     'trip': trip ,
     'peoples': peoples_trip_doesnt_have
     }
    )

class PeopleList(ListView, LoginRequiredMixin):
  model = People


class PeopleDetail(DetailView, LoginRequiredMixin):
  model = People

class PeopleCreate(CreateView, LoginRequiredMixin):
  model = People
  fields = '__all__'

class PeopleUpdate(UpdateView, LoginRequiredMixin):
  model = People
  fields = ['name', 'relation']

class PeopleDelete(DeleteView, LoginRequiredMixin):
  model = People
  success_url = '/peoples/'


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



