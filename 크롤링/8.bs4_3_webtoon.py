import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title= cartoons[0].get_text()
# link =cartoons[0].a["href"]

for c in cartoons:
    title = c.a.get_text()
    link = "https://comic.naver.com"+c.a["href"]
    print(title+link)