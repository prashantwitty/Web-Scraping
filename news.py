from bs4 import BeautifulSoup as bs
import requests
num=range(0,14)
count=1
for i in num:
    link=('https://www.indiatoday.in/top-stories?page={}'.format(i))
    res=requests.get(link)
    soup=bs(res.text,'lxml')
    news=soup.find('div',{'class':"view view-category-wise-content-list view-id-category_wise_content_list view-display-id-section_wise_content_listing view-dom-id- custom"})
    headlines=news.find_all('h2')
    for headline in (headlines):
        if headline.text=='Pages':
            continue
        print(str(count)+') ',headline.text)
        print()
        count+=1