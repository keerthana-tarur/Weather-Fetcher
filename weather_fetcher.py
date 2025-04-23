import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']} ({data['sys']['country']}):")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or API error. Please check your input and API key.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, key)
