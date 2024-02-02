#importing necessary libraries

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

#setting up service and driver
s=Service("D:/Coding stuffs/WebScrapping/Selenium/driver/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

#initiating automation
driver.get("https://www.google.com/")
#time.sleep()
input= driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
input.send_keys("Selenium")
#time.sleep(10)
input.send_keys(Keys.ENTER)
time.sleep(5)