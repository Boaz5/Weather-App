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
        
        if data['cod'] != 200:
            raise ValueError(f"OpenWeatherMap API Error: {data['cod']} : {data['message']}")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        return None
    except ValueError as val_err:
        print(val_err)
        return None
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return None
    
    return data


if __name__ == "__main__":
    data = get_weatherData(1)
    print(data)