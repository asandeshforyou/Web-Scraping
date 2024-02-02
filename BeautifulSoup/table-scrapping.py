import requests
from bs4 import BeautifulSoup
import pandas as pd


url="https://ticker.finology.in/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')


table=soup.find("table",class_="table table-sm table-hover screenertable")

#defining lists to store data

data=[]
headers=[]

#getting table headers

for th in table.find_all('th'):
    headers.append(th.text.strip())

#getting table rows

for row in table.find_all('tr')[1:]:
    rowData=[td.text.strip() for td in row.find_all('td')]
    data.append(rowData)


#creating a dataframe using pandas
df=pd.DataFrame(data,columns=headers)

#print(df)

df.to_excel("stock_data.xlsx")
df.to_csv("stock_data.csv")
    
    
    


