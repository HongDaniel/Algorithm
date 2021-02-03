import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=3&backgroundColor="
h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get(url,headers=h)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
# print(items[0].find("div",attrs={"class":"name"}).get_text())

for i in items:
    ad_badge =  i.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge : 
        print("<광고 상품제외합니다.")
        continue
    name = i.find("div",attrs={"class":"name"}).get_text()
    price = i.find("strong",attrs={"class":"price-value"}).get_text()
    print(name+price)