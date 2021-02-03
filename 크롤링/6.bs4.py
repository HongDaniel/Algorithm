import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #처음으로 발견되는 a
#print(soup.a.attrs) # a element의 속성 정보
#print(soup.find("li", attrs = {"class":"rank01"})) # li - tag type, attrs - 속성
rank1=soup.find("li", attrs = {"class":"rank01"})
#print(rank1.a.get_text())
#print(rank1.next_sibling)
#rank2=rank1.next_sibling.next_sibling
#print(rank2)
#print(rank1.parent)
#rank2=rank1.find_next_sibling()
#print(rank2.a.get_text())
#rank3=rank2.find_next_sibling()
#print(rank3.a.get_text())
print(rank1.find_next_siblings("li"))