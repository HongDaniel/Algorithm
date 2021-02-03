import requests
import csv
from bs4 import BeautifulSoup


h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
url ="https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "네이버-시가총액(200위까지).csv"
f=open(filename,'w', encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page),headers=h)
    res.raise_for_status()
    soup= BeautifulSoup(res.text,"lxml")

    rows =soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) <= 1: continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)