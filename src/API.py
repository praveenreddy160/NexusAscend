import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# print(longitude, latitude)

def my_location():
    my_lax = 17.385044
    my_lng = 78.486671
    Parameters = {
        "lat": my_lax,
        "lng": my_lng,
        "formatted": 0  # Use 0 for unformatted (ISO 8601) times, 1 for formatted times
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=Parameters)
    response.raise_for_status()
    data = response.json()
    sun_rise = data["results"] ["sunrise"]
    sun_set = data ["results"] [ "sunset"]
    print(sun_rise, sun_set)

my_location()