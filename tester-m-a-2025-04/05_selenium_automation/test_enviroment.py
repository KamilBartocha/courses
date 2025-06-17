from selenium import webdriver
from time import sleep

driver = webdriver.Safari()
print(driver)
driver.get("https://onet.pl/")
sleep(5)
site_title = driver.title
print(site_title)
assert site_title == "Onet – Jesteś na bieżąco"
sleep(5) # Czekaj 5 sekund
