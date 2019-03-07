
import time 
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_options = Options()  
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/parthabhattacharjee/node_modules/chromedriver/lib/chromedriver/chromedriver", chrome_options=chrome_options)

# driver.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=MRF&illiquid=0&smeFlag=0&itpFlag=0")
# content = driver.page_source
# soup = BeautifulSoup(content, 'html.parser')
# lastPrice = soup.find("span", id="lastPrice")
# print ( lastPrice.text )

driver.get("https://www.nseindia.com/")

# search = driver.find_element_by_css_selector(".gLFyf gsfi")

search = driver.find_element_by_id("keyword") 
search.clear() 
search.send_keys("M&M")
time.sleep(2)
search.send_keys(Keys.RETURN)


lastPrice = driver.find_element_by_id("lastPrice") 
print (lastPrice.text )

time.sleep(2)
div = driver.find_element_by_id("show-hide") 
div.click()

time.sleep(2)
deliveryToTradedQuantity = driver.find_element_by_id("deliveryToTradedQuantity") 
print (deliveryToTradedQuantity.text )

time.sleep(10)

driver.close()
