import requests
from dotenv import load_dotenv
import os

# Load environment variables and New York Times API key\n",
load_dotenv(verbose=True, override=True, dotenv_path='example.env')
api_key = os.getenv("WEATHER_API_KEY_2")

city = 'Denver'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
response = requests.get(url)
weather_json = response.json()

# print(weather_json)

location = weather_json.get('location')
name = location.get('name')
region = location.get('region')
current = weather_json.get('current')
temp = current.get('temp_f')
descr = current.get('condition').get('text')

print(name, region, temp, descr, sep=', ')
