import requests


def check_url(url):
    print("Checking connectivity ")
    response = requests.get(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was: {response.status_code}")


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")
check_url(input_url)
