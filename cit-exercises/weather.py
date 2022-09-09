# openweatherapi example
# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=f4b158f1cdfc434fd2fb00ca2741553d

# city name as input and weather as output
# save city name and current weather to file
# read file and display contents

import requests

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter a city whose weather you want: ")
API_KEY = "f4b158f1cdfc434fd2fb00ca2741553d"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()

   # getting weather
   temperature = int(data['main']['temp'] - 273)
   weather = data['weather'][0]['description']
   print(f"The weather of {CITY} is as follows:")
   print(f"Temperature: {temperature}")
   print(f"Weather: {weather}")

   # adding weather to a file
   # run program in current folder
   f = open("cities_weather.txt", "a")
   f.write(f"{CITY} : {temperature} degrees celsius, {weather} weather \n")
   f.close()
else:
   # showing the error message
   print("Error in the HTTP request")