'''
Weather API programmed by Isaiah Romero
ESYST-131 IoT - Python Programming 
5/25/22
Creating a weather API
Libraries being used are requests

'''

import requests


'''
Variables
city
API_Key - personal API Key for Weather
tempK - weather in kelvin
tempF - weather in fahrenheit
windS - wind speed
windD - wind direction
Functions
getWeather() - callable function to get weather
'''

#TODO
#Request to API
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

#func getWeather()
    #user's city
    #request > API 
    #test / print API
    #formatting JSON Response
#Conversions
#print

def getWeather(): 
    #vars
    
    city = input("Please enter a city: ")
    API_key = 'cf93c4423693ba49fb02e96f58dcd5c4'
    API_req = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
    
    json_data = requests.get(API_req).json()
    print(json_data)
    
    #Print current weather
    currWeather = json_data['weather'][0]['main']
    print(f'Current weather: {currWeather}')

    #Print current temperature and imperial temperature
    tempK = json_data['main']['temp']
    print(f'Current temperature: {tempK}')
    tempF = (tempK-273.15) * 9 / 5 + 32
    print(f'Current temperature in fahrenheit: {tempF}')

    #Print wind speed and direction
    windS = json_data['wind']['speed']
    print(f'Current wind speed: {windS}')
    windD = json_data['wind']['deg']
    print(f'Current wind direction: {windD}')
#tempF - conversion  (K-273.15) * 9 / 5 + 32 = F
#wind
#TODO
#low - high temp


#Call getWeather()
getWeather()