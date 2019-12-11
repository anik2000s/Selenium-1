from selenium import webdriver
browser = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver") # Place where chromedriver is located
browser.get('http://www.google.com/')
elem = browser.find_element_by_name('q')
elem.send_keys('cats')
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)