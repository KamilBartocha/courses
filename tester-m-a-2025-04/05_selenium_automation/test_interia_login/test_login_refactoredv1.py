from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_to_interia_poczta(driver, email, password):
    driver.get("https://poczta.interia.pl/logowanie/")
    sleep(3)

    rodo_agree_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    rodo_agree_button.click()

    email_form = driver.find_element(By.ID, "email")
    email_form.click()
    email_form.send_keys(email)

    pass_form = driver.find_element(By.ID, "password")
    pass_form.click()
    pass_form.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "btn--login")
    login_button.click()

def test_login_into_interia_poczta_success():
    driver = webdriver.Safari()
    login_to_interia_poczta(driver, "code.brainers.tester@interia.pl", "testerZAQ!2wsx")
    sleep(5)
    assert driver.title == "Poczta w Interii"
    driver.quit()

def test_login_into_interia_poczta_wrong_credentials():
    """Błędny e-mail lub hasło. after loging in with wrong credentials"""
    driver = webdriver.Safari()
    login_to_interia_poczta(driver, "code.brainers.tester@interia.pl", "tester_not_existing")
    sleep(5)
    form_error = driver.find_element(By.CLASS_NAME, "form__error")
    assert form_error.text == "Błędny e-mail lub hasło."
    driver.quit()
