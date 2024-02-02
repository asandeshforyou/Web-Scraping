import requests
from bs4 import BeautifulSoup

url='https://www.daraz.com.np/smartphones/?spm=a2a0e.11779170.cate_5.1.6fe22d2bYJZSfM'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
test=soup.find("div",class_="title-wrapper--IaQ0m")
print(test)
