
import urllib.request
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "https://athena-dot-symphony-qa-performance.appspot.com/apdex/619d1af2-3413-4ee6-bc6f-9be5884ed7d0/index.html"


#CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver.exe"
CHROME_DRIVER_PATH = "usr/local/bin/chromedriver"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=%s" %WINDOW_SIZE)

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
browser.get(link)
delay = 10

tb = browser.find_element_by_id("statisticsTable")
if tb is None:
    print("not existed")
else:
    rows = tb.find_elements(By.TAG_NAME,"tr")
    for row in rows:        
        cols = row.find_elements(By.TAG_NAME,"td")
        if (len(cols) > 0):
            print(cols[0].text)        
    
print(browser.title)