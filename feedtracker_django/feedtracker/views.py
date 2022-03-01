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

@login_required
def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horse_list.html')
    
@login_required
def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    feedings = Feeding.objects.all()

    
@login_required
def add_a_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        add_feeding = form.save(commit=False)
        add_feeding = add_feeding.horse_id
        add_feeding.save()
    return redirect('horse_detail', horse_id=horse_id)


#class based views
class Create_Horse(LoginRequiredMixin, CreateView):
    model = Horse
    fields = ['name', 'age', 'weight', 'height']

class Update_Horse(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = ['name', 'age', 'weight', 'height']

class Delete_Horse(LoginRequiredMixin, DeleteView):
    model = Horse
    success_url = '/horses/'

class Update_Feeding(LoginRequiredMixin, UpdateView):
    model = Feeding
    fields = ['meal_time', 'hay', 'alfalfa', 'grain',]
    
class Delete_Feeding(LoginRequiredMixin, DeleteView):
     model = Feeding
     success_url = 'horse/<int:horse_id>/'