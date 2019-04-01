from bs4 import BeautifulSoup as bs
import requests
num=range(1,10)
for i in num:
    link=('http://quotes.toscrape.com/page/{}/'.format(i))
    res=requests.get(link)
    soup=bs(res.text,'lxml')
    quotes=soup.find_all('span',{'class':'text'})
    authors=soup.find_all('small',{'class':'author'})
    for quote,author in zip(quotes,authors):
        print(quote.text)
        print('--- '+author.text)