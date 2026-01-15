"""
- Logika logowania przeniesiona do osobnej funkcji
- test z logowaniem_sucess używa tej funkcji
- dodatkowy test z logowaniem złymi danymi
czas: ok 20sec
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

poczta_url = "https://poczta.interia.pl/logowanie"

def _login_into_interia(driver, email, password):
    driver.maximize_window()
    driver.get(url=poczta_url)
    sleep(4)
    rodo_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    rodo_button.click()
    sleep(3)

    form_user_email = driver.find_element(By.ID, "email")
    form_user_email.click()
    form_user_email.send_keys(email)

    form_password = driver.find_element(By.ID, "password")
    form_password.click()
    form_password.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "btn--login")
    login_button.click()
    sleep(6)


def test_interia_login_correct_cred():
    driver = webdriver.Safari()
    _login_into_interia(driver, "code.brainers.tester@interia.pl", "testerZAQ!2wsx")
    assert "Poczta w Interii" in driver.title
    driver.quit()


def test_interia_login_wrong_cred():
    driver = webdriver.Safari()
    _login_into_interia(driver, "wrong_email_test@interia.pl", "not_existing")
    assert driver.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    form_error = driver.find_element(By.CLASS_NAME, "form__error")
    assert form_error.text == "Błędny e-mail lub hasło."
    driver.quit()
