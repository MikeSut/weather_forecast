import requests
import json
city = 'Омск'


url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+\
      '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

#json с погодными данными
weather_data_structure = json.dumps(requests.get(url).json(), indent=2)

weather_data = requests.get(url).json()

temperature = round(weather_data['main']['temp'])
wind_speed = weather_data["wind"]["speed"]

print('Сейчас в городе', city, str(temperature), '°C')
print('Скорость ветра -', str(wind_speed), 'м/с.')