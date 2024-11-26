from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Safari()
driver.get("https://google.com")
print(driver.title)
driver.implicitly_wait(3)
accept_all = driver.find_element(By.ID, "L2AGLb")
accept_all.click()  # id="L2AGLb"

driver.implicitly_wait(3)
search = driver.find_element(By.ID, "APjFqb")
search.send_keys("selenium test")

driver.implicitly_wait(3)
search.send_keys(Keys.RETURN)

sleep(4)

results = driver.find_element(By.ID, "result-stats")
print(results.text)

assert results.text is not None
driver.quit()
