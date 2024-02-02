import requests
import pandas as pd
from bs4 import BeautifulSoup


url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

titles=soup.find_all("a",class_="title")
productNames=[]
for i in titles:
    title=i.text
    productNames.append(title)
#print(productNames)

prices=soup.find_all("h4",class_="float-end price card-title pull-right")
productPrices=[]

for i in prices:
    price=i.text
    productPrices.append(price)
#print(productPrices)

descriptions=soup.find_all("p",class_="description card-text")
productDescriptions=[]
for i in descriptions:
    description=i.text
    productDescriptions.append(description)

#print(productDescriptions)

dataFrame=pd.DataFrame({"Product Name":productNames,"Descrption":productDescriptions,"Price":productPrices})
#print(dataFrame)

#dataFrame.to_csv("E:\product_details.csv")
dataFrame.to_excel("E:\product_details.xlsx")
