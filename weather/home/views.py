from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    # city = "gachibowli"
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d97ac08b580abf51fce6901ee97bedd4'
    data = requests.get(url)
    resp = data.json()
    
    payload = {'city':resp['name'],
               'weather': resp['weather'][0]['main'],
               'icon' : resp['weather'][0]['icon'],
               'kelvin_tempreture':round(resp['main']['temp']),
               'celcious_tempreture':round(resp['main']['temp']) - 273,
               }
    
    context = {'resp': payload}
    print(context)
    return render(request,'home.html', context)