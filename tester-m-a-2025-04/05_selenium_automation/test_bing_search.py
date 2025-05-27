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
text_area.send_keys("test selenium")
sleep(2)

#WHEN "ENTER" is pressed (search request)
text_area.send_keys(Keys.ENTER)
sleep(5)


#THEN wiecej element is visable on the screen
wiecej = driver.find_element(By.ID, "b_tween_searchResults")
sleep(4)
print(wiecej.text)
assert wiecej.text.startswith("About")

driver.quit()