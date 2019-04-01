from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\webdrivers\chromedriver.exe')
driver.get('https://www.hackerearth.com/challenges/')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(res, 'lxml')
box = soup.find('div', {'class': 'upcoming challenge-list'})

all_hackathons = box.find_all('div', {'class': 'challenge-card-modern'})
print('\nNew upcoming Hackathon challenges are listed below !')

for count,hackathon in enumerate(all_hackathons,1):
    h_type = hackathon.find('div', {'class': 'challenge-type'}).text.replace('\n', '')
    name = hackathon.find('div', {'class': 'challenge-name'}).text.replace('\n', '')
    date = hackathon.find('div', {'class': 'date'}).text.replace('\n', '')

    print('\n',str(count)+')',h_type, name, date)