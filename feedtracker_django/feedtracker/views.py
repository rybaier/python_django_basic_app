import os
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
from .models import Horse, Feeding
from .forms import FeedingForm, HorseForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# .filter(user=request.user)
def horse_index(request):
    horses = Horse.objects.filter(user=request.user)
    return render(request, 'horses/horse_list.html', { 'horses':horses })
    

def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    feedings = Feeding.objects.filter(horse=horse)
    return render(request, 'horses/horse_detail.html', {'horse': horse, 'feedings': feedings})

def feeding_index(request):
    feedings = Feeding.objects.all()
    return render(request, 'feedtracker/feeding_list.html')
    

def add_a_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        add_feeding = form.save(commit=False)
        add_feeding = add_feeding.horse_id
        add_feeding.save()
    return redirect('horses/horse_detail', horse_id=horse_id)


#class based views
class Create_Horse(LoginRequiredMixin, CreateView):
    model = Horse
    fields = ['name', 'age', 'breed', 'markings', 'weight', 'height']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update_Horse(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = ['name', 'age', 'breed', 'markings', 'weight', 'height']

class Delete_Horse(LoginRequiredMixin, DeleteView):
    model = Horse
    success_url = '/horses/'

class Create_Feeding(LoginRequiredMixin, CreateView):
    model = Feeding
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form), 

class Update_Feeding(LoginRequiredMixin, UpdateView):
    model = Feeding
    fields = ['meal_time', 'hay', 'alfalfa', 'grain',]
    
class Delete_Feeding(LoginRequiredMixin, DeleteView):
     model = Feeding
     success_url = redirect('horse/<int:horse_id>/')


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