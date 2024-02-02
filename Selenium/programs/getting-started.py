from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s=Service("D:/driver/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)


driver.get("https://www.tutorialsfreak.com/")

driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button").click()

time.sleep(20)
