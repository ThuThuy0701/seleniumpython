from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
s = Service("C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://alonhadat.com.vn/")
driver.maximize_window()
time.sleep(10)
#print tiltle of website
title = driver.title
print(title)
driver.execute_script("window.scrollBy(0,900)","")
time.sleep(3)
# show the first 20 pieces of information on some outstanding real estate
contents = driver.find_elements(By.XPATH,"//div[@class='vip-properties']/div[@class='item']")
print(len(contents))
print("Một số bất động sản nổi bật")
i=1
for content in contents:
    print(i,".",content.text)
    i+=1
# Mở 1 bất động sản cụ thể và lấy thông tin chi tiêt của bất động sản đó
driver.get("https://alonhadat.com.vn/ban-nha-nghia-hung-phuong-6-tan-binh-50m2-5-lau-6pn-gia-giam-con-6-ty-1-12414989.html")
print(driver.title)
time.sleep(3)
content1= driver.find_element(By.XPATH,"//div[@class='property']/div[@class='detail text-content']")
print(content1.text)
print("Các thông tin khác")
rows = driver.find_elements(By.XPATH,"//table/tbody//tr")
countrow = 0
for row in rows:
    countrow+=1
print("Total of row in the website: ",countrow)
for i in range(1,countrow+1):
    for j in range (1,countrow+2):
        data1 = driver.find_element(By.XPATH,"//table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(data1, end="|")
    print()

