from bs4 import BeautifulSoup
import requests
string=''' 
          1. hindi
          2. english
          3. tamil
          4. punjabi
          5. marathi
          6. telugu
          7. gujrati
          8. bengali
          9. bhojpuri
          10. kannada
          11. haryanvi
          12. malyalam
          13. odia
          14. rajasthani
          15. urdu
          16. assamese
       '''
print('\n Which Language do you prefer')
lang=input(string)
flag=True
while (flag==True):
    if (lang=='hindi' or lang=='english' or lang=='tamil' or lang=='punjabi' or lang=='marathi' or lang=='telugu' or lang=='gujrati' or lang=='bengali' or lang=='bhojpuri' or lang=='kannada' or lang=='haryanvi' or lang=='malyalam' or lang=='odia' or lang=='rajasthani' or lang=='urdu' or lang=='assamese'):
        link=('https://www.saavn.com/s/featured/{}/Weekly_Top_Songs'.format(lang))
        flag=False
    else:
         print('\n Enter Above listed languages only')
         lang=input(string)
         flag==True
if flag==False:
    print('Here is the list of top {} songs :'.format(lang))
    print()
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find('ol', {'class': 'content-list'})
    all_songs = data.find_all('div', {'class': 'details'})
    for count, s in enumerate(all_songs, 1):
        song = s.find('p', {'class': 'song-name ellip'})
        print(str(count)+')' ,song.text)