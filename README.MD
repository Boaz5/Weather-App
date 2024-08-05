# Task: Integrate the Weather API to Display Current Weather Information Documentation
>Documents on how to setup and run the application

## Setup Requirements

**NOTE**: Make sure that Python and PIP are installed (Pip should naturally come with Python installation)

- [Setting Up OpenWeatherMap API](#OpenWeatherMap-API-Setup)
- [Setting Up Python Virtual Environment](#Virtual-Environment-Setup)
- [Setting Up .env File](#.env-Setup)
- [Installation](#Installation)

## OpenWeatherMap API Setup

* Create an OpenWeatherMap account at https://openweathermap.org.
* Create an OpenWeatherMap key at https://home.openweathermap.org/api_keys.
* Save the Key

## Virtual Environment Setup

**NOTE**: Use pip if on Windows and pip3 on Mac or Linux
* Install 'virtualenv' if it's not already installed
'''sh
pip install virtualenv
'''
* Navigate to the directory that you want this application to be in and run 
'''
On Windows:
python -m venv <environment name>
On Mac/Linux:
python3 -m venv <environment name>
example: python -m venv .venv
'''
**note** Don't include the <>
* Activate the virtual environment
  * <venv name>\Scripts\activate (On Windows)
  * source <venv name>/bin/activate

## .env Setup

A good habit to have to make your program safer is to store all your API keys in a file called .env

## Installation

Use pip or pip3 to install all the dependencies

