from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

#GIVEN "test selenium" is typed into search on site bing.com
driver = webdriver.Safari()
driver.get("https://www.bing.com/")
sleep(2)

text_area = driver.find_element(By.ID , "sb_form_q")
sleep(2)
text_area.click()
sleep(2)
text_area.send_keys("selenium")
sleep(1)

#WHEN "ENTER" is pressed (search request)
text_area.send_keys(Keys.ENTER)
sleep(2)


#THEN wiecej element is visable on the screen
wiecej = driver.find_element(By.ID, "b-scopeListItem-menu")
sleep(4)
print(wiecej)
assert wiecej is not None

driver.quit()