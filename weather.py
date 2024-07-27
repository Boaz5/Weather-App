import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('API_KEY')


def get_weatherData(city):
    # openweathermap api request url
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&limit=1&appid={api_key}"
    try:
        response = requests.get(url)

        data = response.json()
        
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None
    
    return data


if __name__ == "__main__":
    data = get_weatherData("las vegas")
    print(data)