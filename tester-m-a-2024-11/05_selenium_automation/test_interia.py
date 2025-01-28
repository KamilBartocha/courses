"""Test poczty interia

Test Scenario:
GIVEN poczta.interia.pl/logowanie is loaded**
AND registered user credentials are typed into login form**

WHEN "Zaloguj się" button is pressed (search request)**

THEN User is logged in and email box is opened**

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_interia_log_in():
    driver = webdriver.Safari()
    driver.get("https://poczta.interia.pl/logowanie")

    sleep(3)
    rodo_agree = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    rodo_agree.click()


    email_form = driver.find_element(By.ID, "email")
    email_form.send_keys("code.brainers.tester@interia.pl")

    pass_form = driver.find_element(By.ID, "password")
    pass_form.send_keys("testerZAQ!2wsx")

    log_in_button = driver.find_element(By.CLASS_NAME, "btn")
    log_in_button.click()
    sleep(3)
    assert driver.title == "Poczta w Interii"
    sleep(3)
    driver.quit()
