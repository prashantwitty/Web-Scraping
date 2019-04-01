from bs4 import BeautifulSoup
import requests
num=range(1,3)
index=1
print()
print('list of Hackathon events are :')
print()
for i in num:
        link=('http://www.hackathon.io/events?page={}'.format(i))
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'lxml')
        hacks = soup.find_all('div', {'class': 'event-teaser'})
        for hack in(hacks):
                time = hack.find('div', {'class': 'two columns time'}).text.replace('\n', '').strip()
                name = hack.find('h4').text.replace('\n', '').strip()
                description = hack.find('h5').text.replace('\n', '').strip()
                location = hack.find('div', {'class': 'two columns location'}).text.replace('\n', '').strip()
                print("{}. {}\n{}\n{}\n{}\n\n".format(str(index),name, description, time, location))
                index+=1