import json
import requests

hakusana = input("Anna kaupungin nimi: ")
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=675cdbbcb9f88c517e4a39e62daf810e")

if response.status_code == 200:
    data = response.json()
    temperature_kelvin = data["main"]["temp"]
    sää_celsius = temperature_kelvin - 273.15
    weather_description = data["weather"][0]["description"]
    print(f"säätila  {hakusana}ssa on {weather_description} ja lämpötila on {sää_celsius:.1f}°C.")
else:
    print("Säätilan hakeminen epäonnistui.")
