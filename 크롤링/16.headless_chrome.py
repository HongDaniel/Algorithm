from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)


#browser.execute_script("window.scrollTo(0,2080)")

import time 
interval = 2

prev_height= browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

from bs4 import BeautifulSoup
import requests

h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36","Accept-Language":"ko-KR,ko"}

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs = {"class":"Vpfmgd"})
for m in movies:
    
    title= m.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price = m.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else :
        continue
      
    final_price= m.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    link= m.find("a",attrs={"class":"JC71ub"}) ["href"]
    link = "https://play.google.com"+link
    
    print("제목 :  {}".format(title))
    print("할인 전 가격 : {}".format(original_price))
    print("최종가격 : {}".format(final_price))
    print("링크 : {}".format(link))
    print("*"*110)
browser.quit()
    

