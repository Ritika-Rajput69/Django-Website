from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('weather_info/', views.weather_info, name='weather_info'),
    path('service/', views.services, name='services'),


    

]