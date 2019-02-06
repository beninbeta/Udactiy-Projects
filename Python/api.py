import requests
API_ROOT = 'https://www.metaweather.com'
API_Location = '/api/location/search/?query='
API_WEATHER = '/api/location/'

def fetch_location(query):
    return requests.get(API_ROOT + API_Location + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def muliple_locations(locations):
    print("Only one locaton please, Did you mean? ")
    for location in locations:
        print(f"\t* {location['title']}")

def diplay_weather(weather):
    print(f"The weather for {weather['title']}:") 
    for entry in weather["consolidated_weather"]:
        date = entry['applicable_date']
        high = entry['max_temp']
        low = entry['min_temp']
        state = entry['weather_state_name']
        print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where would you like a forescat for? ")
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is")
        elif len(locations) > 1:
            muliple_locations(locations)
        else:
            woeid = locations[0]['woeid']
            diplay_weather(fetch_weather(woeid))   
         
    except requests.exceptions.ConnectionError:
        print("There was a connection error! Could not connect to the server.")

if __name__ == '__main__':
    while True:
        weather_dialog()