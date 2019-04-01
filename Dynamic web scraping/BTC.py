from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\webdrivers\chromedriver.exe')
driver.get('http://livebtcprice.com/')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
table=soup.find('table',{'class':'index'})
all_cur=table.find_all('tr')
print("['Convertor' , 'Price' , 'Currency' , '%Change', 'High' , 'Low' ]")
for tr in all_cur:
    td=tr.find_all('td')
    td= [ele.text.strip() for ele in td]
    print([ele for ele in td if ele])