from django.shortcuts import render, HttpResponse

# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d42a311b6d228511f3ae95bdaff33361"
        list_of_data = request.get(source.format(city)).json()

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' +str(list_of_data['coord']['lat']),
            "temp": round((list_of_data['main']['temp']- 32) * 5.0/0.2),
            "humidity": str(list_of_data['main']['humidity'])
        }
    else:
        data = {}
        return render(request, "weather.html", data)
    
        

