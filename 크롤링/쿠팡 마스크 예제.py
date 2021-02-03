import requests
from bs4 import BeautifulSoup
import re

h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


for page in range(1,6):
    print("페이지 : ",page)
    url = "https://www.coupang.com/np/search?q=%EB%A7%88%EC%8A%A4%ED%81%AC&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(page)
    res = requests.get(url,headers=h)
    res.raise_for_status

    soup = BeautifulSoup(res.text,"lxml")
    masks = soup.find_all("li",attrs={"class":re.compile("^search-product")})


    for i in masks :
        ad = i.find("span",attrs={"class":"ad-badge-text"})

        if ad:
            #print("<광고상품 제외>")
            continue

        stock = i.find("div",attrs={"class":"out-of-stock"})
        if stock:
            continue

        name = i.find("div",attrs={"class":"name"}).get_text()
        price = i.find("strong",attrs={"class":"price-value"}).get_text()
        rating = i.find("em", attrs={"class":"rating"})
        
        if rating:
            rating = i.find("em", attrs={"class":"rating"}).get_text()
        
        else:
            print("평가 안됨")
            continue 
        
        review = i.find("span",attrs={"class":"rating-total-count"})
        
        if rating:
            review = i.find("span",attrs={"class":"rating-total-count"}).get_text()
        
        else:
            print("평가원 없음")
            continue 

        if int(review[1:-1])>=100 and float(rating)>=4.5:
            print("상품명 : ", name)
            print("상품가격 : ", price)
            print("상품평 : ", rating)
            print("리뷰한 사람 : ", review[1:-1])
            print("*"*100)
    print("-.-.-.-"*100)


