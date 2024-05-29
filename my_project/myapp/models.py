from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=125)
    email=models.CharField(max_length=125)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField(null=True)



class WeatherData(models.Model):
    city = models.CharField(max_length=50)
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    # Add other weather data fields as needed
