import requests 


url = "http://nadocoding.tistory.com"
headers = {"user-agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print("응답코드: ",res.status_code)
