import requests
from bs4 import BeautifulSoup

url ="https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
h = {"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res= requests.get(url,headers=h)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
rows = soup.find("table",attrs = {"class":"tbl"}).find("tbody").find_all("tr")

for i, row in enumerate(rows):
    print(f"========= 매물 {i+1} =========")
    kind = row.find("td", attrs = {"class":"col1"}).get_text().strip()
    area = row.find("td", attrs = {"class":"col2"}).get_text().strip()
    price = row.find("td", attrs = {"class":"col3"}).get_text().strip()
    dong = row.find("td", attrs = {"class":"col4"}).get_text().strip()
    floor = row.find("td", attrs = {"class":"col5"}).get_text().strip()
    print("거래 : {}".format(kind))
    print("면적 : {} (공급/전용)".format(area)) 
    print("가격 : {} (만원)".format(price))
    print("동 : {}".format(dong))
    print("층 : {}".format(floor))
