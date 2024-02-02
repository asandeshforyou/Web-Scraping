

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://webscraper.io/test-sites/e-commerce/static/phones/touch'
phoneName=[]
descriptions=[]
phonePrices=[]
for pages in range(1,3):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    #for phone titles
    Titles=soup.find_all("a",class_="title")
    for title in Titles:
        phoneName.append(title.text)
    #for phone's description
    descs=soup.find_all("p",class_="description card-text")
    for desc in descs:
        descriptions.append(desc.text)
    
    #for phone's price
    prices=soup.find_all("h4",class_="float-end price card-title pull-right")
    for price in prices:
        phonePrices.append(price.text)

    

    #getting url of next page from next button
    nextPage=soup.find("a",class_="page-link").get("href")
    newURL="https://webscraper.io"+nextPage
    url=newURL
    #print(url)

data={'Title':phoneName,'Description':descriptions,'Price':phonePrices}

df=pd.DataFrame(data)
print(df)