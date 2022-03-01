from django import forms 
from .models import Horse, Feeding

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ('meal_time', 'hay', 'alfalfa', 'grain',)

class HorseForm(forms.ModelForm):
    model = Horse
    fields = ('name', 'age', 'weight', 'height',)