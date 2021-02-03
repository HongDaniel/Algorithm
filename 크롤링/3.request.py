import requests 

res = requests.get("http://naver.com")
res.raise_for_status()
print("응답코드: ",res.status_code)
