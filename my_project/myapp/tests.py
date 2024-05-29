from django.test import TestCase, Client
from myapp.views import index, weather_info, contact
from myapp.models import Contact, WeatherData
from myapp.forms import ContactForm, WeatherForm
from django.shortcuts import reverse

client = Client()


class MyappViewsTest(TestCase):

    # def test_index_view_get(self):
    #     response = client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'index.html')
    #     self.assertContains(response, 'This is context ')  # Check for context variable

    # def test_services_view_get(self):
    #     response = client.get('/services/')
    #     self.assertEqual(response.status_code, 404)
    #     self.assertTemplateUsed(response, 'services.html')

    # def test_weather_info_view_get(self):
    #     response = client.get('/weather_info/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'weather_info.html')
    #     self.assertIsInstance(response.context['form'], WeatherForm)  # Check for form instance

    # def test_weather_info_view_post_valid(self):
    #     # Simulate a valid form submission with city name
    #     data = {'city': 'London'}
    #     response = client.post('/weather_info/', data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('weather_info'))

    #     # Since the actual weather data retrieval involves external API calls,
    #     # we can't guarantee a successful save in all test cases.
    #     # However, we can check if the form is valid and data is processed correctly in the view.
    #     self.assertTrue(response.context_data.get('form').is_valid())  # Check form validity from context (avoids accessing potentially empty request.context)
    #     self.assertContains(response, 'Weather Information now visible....!')  # Check for success message

    # def test_weather_info_view_post_invalid(self):
    #     """Tests the weather_info view with an invalid POST request"""
    #     # Simulate an invalid form submission with an empty city name
    #     data = {'city': ''}
    #     response = client.post('/weather_info/', data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'weather_info.html')
    #     self.assertFalse(response.context_data.get('form').is_valid())  # Check form validity from context
    #     self.assertContains(response, 'Invalid city entered.')  # Check for error message

    def test_contact_view_get(self):
        response = client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)  # Check for form instance

    # def test_contact_view_post_valid(self):
    #     # Simulate a valid form submission with contact details
    #     data = {'name': 'Ritika', 'email': 'ritikasingh@gmail.com',
    #             'phone': '1234567890', 'desc': 'This is a test message'}
    #     response = client.post('/contact/', data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('contact'))

    #     # Check if a new Contact object is created
    #     self.assertEqual(Contact.objects.count(), 1)
    #     contact = Contact.objects.last()
    #     self.assertEqual(contact.name, 'Ritika')
    #     self.assertEqual(contact.email, 'ritikasingh@gmail.com')
    #     self.assertEqual(contact.phone, '1234567890')
    #     self.assertEqual(contact.desc, 'This is a test message')

from django.urls import resolve, reverse
from myapp import views

class UrlTests(TestCase):

    def test_home_url_resolves(self):
        """Tests if the path '/' resolves to the index view"""
        url = resolve('/')
        self.assertEqual(url.func, views.index)

    def test_home_url(self):
        """Tests if you can reverse the URL name 'home' to '/'"""
        self.assertEqual(reverse('home'), '/')

    def test_contact_url_resolves(self):
        """Tests if the path '/contact/' resolves to the contact view"""
        url = resolve('/contact/')
        self.assertEqual(url.func, views.contact)

    def test_contact_url(self):
        """Tests if you can reverse the URL name 'contact' to '/contact/'"""
        self.assertEqual(reverse('contact'), '/contact/')

    def test_weather_info_url_resolves(self):
        """Tests if the path '/weather_info/' resolves to the weather_info view"""
        url = resolve('/weather_info/')
        self.assertEqual(url.func, views.weather_info)

    def test_weather_info_url(self):
        """Tests if you can reverse the URL name 'weather_info' to '/weather_info/'"""
        self.assertEqual(reverse('weather_info'), '/weather_info/')

    def test_services_url_resolves(self):
        """Tests if the path '/service/' resolves to the services view"""
        url = resolve('/service/')
        self.assertEqual(url.func, views.services)

    def test_services_url(self):
        """Tests if you can reverse the URL name 'services' to '/service/'"""
        self.assertEqual(reverse('services'), '/service/')
