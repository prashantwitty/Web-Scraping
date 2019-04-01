from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import urllib.request

res = requests.get('https://bing.wallpaper.pics/')
soup = BeautifulSoup(res.text, 'lxml')

image_box = soup.find('a', {'class': 'cursor_zoom'})
image = image_box.find('img')

link = image['src']

filename = dt.now().strftime('%d-%m-%y.jpg')
urllib.request.urlretrieve(link, filename)