import requests

def get_current_weather(city):
    base_url = f"http://wttr.in/{city}?format=j1"
    response = requests.get(base_url)
    data = response.json()
    return f"The current temprature in {city} is {data['current_condition'][0]['temp_C']}°C. Feels like: {data['current_condition'][0]['FeelsLikeC']}°C"
