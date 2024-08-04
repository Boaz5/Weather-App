import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('API_KEY')


# Function to send the API request
def api_request(url: str):
    try:
        response = requests.get(url)

        data = response.json()
        
        return data
    
    # Catch any other errors that wasn't caused by misinputs
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    return None


# Function to retrieve weather data from our requested city or zip
def get_weatherData(city: str, zip_code: str):
    # openweathermap api request url
    city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&limit=1&appid={api_key}"
    zip_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units=imperial&appid={api_key}"
    
    
    # Zip will take prio first for API Request
    data = api_request(zip_url)
    
    # If API request for Zip fails then we try using city
    if not data or data['cod'] != 200:
        data = api_request(city_url)
        
    return data


# Function to return the local timezone of where the server is hosted 
def getTime():
    now = datetime.now()
    
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%H:%M")
    return (date, time)


if __name__ == "__main__":
    data = get_weatherData(city = "Las Vegas", zip_code = "")
    print(getTime())
    print(data)