from django import forms
from .models import Contact, WeatherData

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email', 'phone', 'desc','date']

class WeatherForm(forms.ModelForm):
  class Meta:
    model = WeatherData
    fields = ['city']  # Only include the city field for user input
