import requests
from bs4 import BeautifulSoup

#establishing http request

#url="https://www.flipkart.com/q/redmi-mobile-phones-under-10000"
#link=soup.find("body").find("div",id="container")#.find("a",class_="_1LKTO3")
url="https://books.toscrape.com/catalogue/page-1.html"

for i in range(1,3):    
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    titles=soup.find_all("h3")
    bookTitle=[]

    for i in titles:
        title=i.text
        bookTitle.append(title)
    
    link=soup.find("li",class_="next").find("a").get("href")
    completeLink="https://books.toscrape.com/catalogue/"+ link
    #print(completeLink)
    url=completeLink
print(bookTitle)