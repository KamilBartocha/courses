"""
Test wyszukiwarki google.com

Test Scenario:
GIVEN  "test selenium" is typed into search on site google.com
WHEN   "ENTER" is pressed (search request)
THEN   Result stats are calculated and visible on screen

### Kolejność szukania elementów strony w html:
search order:
1. id
2. class
3. name
<button id="L2AGLb" class="tHlp8d
search text form  id="APjFqb" maxlength="2048" n
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#GIVEN
driver = webdriver.Safari()
driver.get("https://google.com")

sleep(2)
button_accept_cookies = driver.find_element(By.ID, "L2AGLb")
button_accept_cookies.click()

search_form = driver.find_element(By.ID, "APjFqb")
search_form.send_keys("test selenium")
# WHEN
search_form.send_keys(Keys.RETURN)
sleep(2)
# THEN
sleep(4)
stats = driver.find_element(By.ID, "result-stats")
assert stats.text is not None

sleep(8)
driver.quit()
