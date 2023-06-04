import requests
from bs4 import BeautifulSoup

url = 'https://www.d20pfsrd.com/bestiary/monster-listings/templates/ectoplasmic-creature-cr-1/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

s = soup.find('div', class_='article-content')

lines = s.find_all('p' or 'ul' or 'h4' or 'li')

linesArray = []
for line in lines:
    linesArray.append(str(line.text))

newlist = []
buljon = 0
for i in range(0, len(linesArray)):
    if linesArray[i].find("CR:") == 0:
        newlist.append(linesArray[i])
        buljon = 1
    elif buljon:
        newlist.append(linesArray[i])
    else:
        pass

for i in range(0,len(newlist)):
    print(newlist[i])
    pass
