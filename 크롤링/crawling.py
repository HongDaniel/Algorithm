from bs4 import BeautifulSoup
from urllib.request import urlopen

response =  urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
f = open("new.txt",'w')
for anchor in soup.select('span.ah_k'):
    print(str(i)+"위: "+anchor.get_text())
    i = i+1
