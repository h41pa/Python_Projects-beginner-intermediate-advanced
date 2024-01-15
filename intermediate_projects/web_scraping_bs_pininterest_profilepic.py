
import requests
from bs4 import BeautifulSoup as bs

youtube_user = input("Input Pininterest User: ")
url = 'https://pinterest.com/' + youtube_user
print(url)
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'class': 'hCL kVc L4E MIw'})['src']
print(profile_image)
