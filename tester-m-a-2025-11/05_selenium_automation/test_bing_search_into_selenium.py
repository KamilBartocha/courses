from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# def test_search_bing_into_selenium():
driver = webdriver.Safari()
driver.get("https://www.bing.com/")
sleep(4)
search_form = driver.find_element(By.ID, "sb_form_q") #id="sb_form_q"
search_form.click()
search_form.send_keys("selenium")
search_form.send_keys(Keys.ENTER)
sleep(2)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium.dev")
link.click()
sleep(5)