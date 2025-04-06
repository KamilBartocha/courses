from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# GIVEN poczta.interia.pl/logowanie is loaded
d = webdriver.Safari()
d.get("https://poczta.interia.pl/logowanie/")
sleep(1)

przejdz_do_sewisu = d.find_element(By.CLASS_NAME, "rodo-popup-agree")
przejdz_do_sewisu.click()
sleep(1)


# AND registered user credentials are typed into login form**
email_form = d.find_element(By.ID, "email")
email_form.send_keys("code.brainers.tester@interia.pl")
sleep(1)

pass_form = d.find_element(By.ID, "password")
pass_form.send_keys("testerZAQ!2wsx")
sleep(1)


# WHEN "Zaloguj się" button is pressed (log request)
zaloguj_sie = d.find_element(By.CLASS_NAME, "btn--login")
zaloguj_sie.click()
sleep(4)

# btns = d.find_elements(By.CLASS_NAME, "btn")
# [
#   <selenium.webdriver.remote.webelement.WebElement (session="BAC9612E-0170-4F89-9C06-682837141BED", element="node-050C1937-530B-4AEF-B8FE-D0505B1E5B10")>,
#   <selenium.webdriver.remote.webelement.WebElement (session="BAC9612E-0170-4F89-9C06-682837141BED", element="node-CAE67003-408D-435C-A295-3BD60529FFCA")>
#]
# btns[0].click()
# btns[1].click()

# THEN User is logged in and email box is opened
title_logged = d.title
title_expected = "Poczta w Interii"
assert title_logged == title_expected

inbox = d.find_element(By.CLASS_NAME, "icon-inbox")
assert inbox is not None

sleep(5)
d.quit()