from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/movies/top"
h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36","Accept-Language":"ko-KR,ko"}
res = requests.get(url,headers=h)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))
#with open("movies.html",'w',encoding="utf-8-sig") as f:
#    f.write(soup.prettify())
for m in movies:
    title = m.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)