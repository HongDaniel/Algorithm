from selenium import webdriver
import time

browser = webdriver.Chrome("chromedriver.exe")

#1. naver로 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click() 


#3. id, pw 입력하기
id = browser.find_element_by_id("id")
id.send_keys("naver")
password = browser.find_element_by_id("pw")
password.send_keys("password")

browser.find_element_by_id("log.login").click()

time.sleep(3)
#4. 로그인 다시하기
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("newid")

print(browser.page_source)
browser.quit()