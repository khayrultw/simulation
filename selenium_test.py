from selenium import webdriver
from bs4 import BeautifulSoup;
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Orion nebula")
time.sleep(1)
elem.submit()
assert "No results found." not in driver.page_source
soup = BeautifulSoup(driver.page_source, "html.parser")
for link in soup.find_all('a'):
        print(link.get('href'))
time.sleep(2)
driver.close()
