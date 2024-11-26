from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

driver = webdriver.Safari()
driver.get("https://poczta.interia.pl/logowanie")
print(driver.title)

# Akceptacja RODO
driver.implicitly_wait(3)
go_to_service = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
go_to_service.click()


# Wpisywanie nazwy e-mail
driver.implicitly_wait(3)
input_email = driver.find_element(By.ID, "email")
input_email.send_keys("code.brainers.tester@interia.pl")


# Wpisywanie hasła
driver.implicitly_wait(3)
input_password = driver.find_element(By.ID, "password")
input_password.send_keys("testerZAQ!2wsx")


# Kliknięcie Zaloguj się
driver.implicitly_wait(3)
button_log_in = driver.find_element(By.CLASS_NAME, "btn")
button_log_in.click()
sleep(4)

print(driver.title)
assert driver.title == "Poczta w Interii"
sleep(10)
driver.quit()