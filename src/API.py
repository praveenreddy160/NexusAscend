import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# print(longitude, latitude)

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    quotes = response.json()
    data = quotes["quote"]
    print(data)
get_quote()