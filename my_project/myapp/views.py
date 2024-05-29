from django.shortcuts import render,HttpResponse,HttpResponseRedirect, reverse
from datetime import datetime
from myapp.models import Contact,WeatherData
from django.contrib import messages
import requests
from .forms import ContactForm,WeatherForm

# Create your views here.
def index(request):
    context ={
        'variable' : "This is context ",
        'variable1': "This is sent by using variable. "
    }
    return render(request,'index.html', context)

def services(request):
    return render(request, 'services.html')





def weather_info(request):
  if request.method == 'POST':
    form = WeatherForm(request.POST) 
    if form.is_valid():
      
      
      city = form.cleaned_data['city']  
      api_key = '7423f2efc5c336f0c7c2803e45198e96'  
      url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' 

      response = requests.get(url)
      

      if response.status_code == 200:
            
            data = response.json()
            city_name = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
          

            context = {
                'city': city_name,
                'temperature': temperature,
                'description': description,
                'error_message': None 
            }


    
      weather = WeatherData(city=city, temperature=temperature, description=description)
      weather.save()  
      messages.success(request, 'Weather Information now visible....!')
      return render(request, 'weather_info.html', context)  
      
    else:
      context = {'form': form, 'error_message': 'Invalid city entered.'}  
      return render(request, 'weather_info.html', context)
  else:
    form = WeatherForm() 
    context = {'form': form, 'error_message': None}  
  return render(request, 'weather_info.html', context)


# main code :---------
# `def contact(request):
#     if request.method =="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         desc=request.POST.get('desc')
    
#         contact=Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
#         contact.save()
#         messages.success(request,'Your message has been sent!')
#         def __str__(self):
#             return self.name()

#     return render(request, 'contact.html')  

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            contact = form.save()  
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect(reverse('contact'))  
        else:
            
            context = {'form': form}
            messages.error(request, 'Please correct the errors below.')  
            return render(request, 'contact.html', context)
    else:
        form = ContactForm()  

    context = {'form': form}
    return render(request, 'contact.html', context)














