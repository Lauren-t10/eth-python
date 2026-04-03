import requests



def get_zurich_weather():
    
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 47.37,
        "longitude": 8.54,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    weather = data["current_weather"]
    mainParams = {
      "Temperature" : weather["temperature"],
      "Wind speed" : weather["windspeed"],  
      "Daytime" : weather["is_day"]
    }
    return mainParams

result = get_zurich_weather()
print(result)

"""
print("Temperature:", weather["temperature"], "celsius")
print("Wind speed:", weather["windspeed"], "km/h")
print("Is daytime:", weather["is_day"])
"""