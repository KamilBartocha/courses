from selenium import webdriver
from time import sleep

driver = webdriver.Safari()
driver.get("https://codebrainers.pl/")
site_title = driver.title
print(site_title)
assert site_title == "CodeBrainers – Prawdopodobnie najlepszy bootcamp w Polsce!"
sleep(5) # Czekaj 5 sekund
driver.quit()
