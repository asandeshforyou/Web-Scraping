#importing required dependencies
import requests
from bs4 import BeautifulSoup
import pandas as pd


#request-response and soup cooking and scraping table

url='https://www.iplt20.com/auction/2022'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find("table",class_="ih-td-tab auction-tbl")


#defining empty lists for header and data

header=[]
data=[]

#getting header
for th in table.find_all('th'):
    header.append(th.text.strip())

#getting table data
for tr in table.find_all('tr')[1:]:
    individualData=[td.text.strip() for td in tr.find_all('td')]
    data.append(individualData)

#creating dataframe using pandas
df=pd.DataFrame(data,columns=header)

#print(df)

df.to_csv('ipl.csv')



