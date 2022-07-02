from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q='+city+'&apiid=28a94848fabd2cd7f23fa6e51a243ebc').read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, 'index.html', data)
