import requests

API_KEY = "215d79ab3fa447ce23b52c34d28ee726"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-272.15, 2)
    print(f"\t City: {city}")
    print(f"\t Country: {data['sys']['country']}")
    print(f"\t Timezone: {data['timezone']}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}")

else:
    print("An error occurred.")