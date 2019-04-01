from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\webdrivers\chromedriver.exe')
count=1
for i in range(1,16):
    link=('https://www.bookmundi.com/india?page={}'.format(i))
    driver.get(link)
    res = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res, 'lxml')
    data=soup.find('div',{'class':'tours-main-holder'})
    box=data.find_all('div',{'class':'trips-holder trips-results'})
    for tour in box:
        trips=tour.find_all('div',{'class':'trips-block thumbnail'})
    count+=1    
    for trip in (trips):
        print(str(count)+'.',' Tour Name :- ',trip.find('h2').text.strip())
        count+=1
        print('Starts/Ends :- ',trip.find('span',{'class':'txt'}).text.replace('View Map','').strip())
        print('Operator :- ',trip.find('span',{'class':'op-title'}).text.strip())
        print('Price :- ',trip.find('mark').text.strip())
        print('Duration :- ',trip.find('span',attrs={'data-original-title': 'Trip Duration'}).text.strip())
        print()