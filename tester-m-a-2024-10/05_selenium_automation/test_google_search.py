from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

# @GIVEN
driver = webdriver.Safari()
driver.get("https://google.com")
driver.implicitly_wait(3)
accept_all = driver.find_element(By.ID, "L2AGLb")
sleep(3)
accept_all.click()  # id="L2AGLb"
search = driver.find_element(By.ID, "APjFqb")
sleep(3)
search.send_keys("selenium test")

# @WHEN
sleep(3)
search.send_keys(Keys.RETURN)

#@THEN
sleep(3)
results = driver.find_element(By.ID, "result-stats")
print(results.text)
assert results.text is not None

driver.quit()
