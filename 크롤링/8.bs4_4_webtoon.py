import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
rating =0 
for c in cartoons:
    rate=c.find("strong").get_text()
    print(rate)
    rating += float(rate)
print("전체점수 : ", rating)
print("평균점수 : ", rating/len(cartoons))
