from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("chromedriver")

url = "https://flight.naver.com/flights/"

browser.get(url)
browser.maximize_window() #창 크게하기

#가는날, 오는날 선택하기 
browser.find_element_by_link_text("가는날 선택").click()
browser.find_elements_by_link_text("25")[0].click()
browser.find_elements_by_link_text("27")[0].click()

#도착지, 항공권 검색
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()

