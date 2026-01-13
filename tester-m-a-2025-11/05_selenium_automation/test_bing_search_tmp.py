from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Safari()
driver.get("https://www.bing.com")
sleep(4)
# <textarea id="sb_form_q" class="sb_form_q" name="q" type="search"...</textarea>
search_form = driver.find_element(By.ID, "sb_form_q")
search_form.click()
search_form.send_keys("selenium alamakota")
search_form.send_keys(Keys.ENTER)
# search_form.send_keys(Keys.RETURN)
sleep(4)
# <span class="sb_count" data-count-target="494000">Liczba wyników — około 494&nbsp;000</span>
results_count = driver.find_element(By.CLASS_NAME, "sb_count")
print(results_count.text)
assert results_count.text.startswith("About") and results_count.text.endswith("results")
sleep(5)
