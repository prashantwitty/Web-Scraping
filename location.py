# getting ip and location 
import requests

res = requests.get('https://ipinfo.io/')
data = res.json()  #converting it into dictionary

city = data['city']
ip=data['ip']


location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]




print('ip : ',ip)
print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City : ", city)