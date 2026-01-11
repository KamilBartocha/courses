"""
- dodanie osobych funkcji do drivera, setup i teardown
- dodanie obsługi wyjątków
- teardown w finally
- implicitly_wait w ustawieniach drivera aby zminimializować sleep
czas ok 10sec
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_driver():
    driver = webdriver.Safari()
    driver.implicitly_wait(5)
    return driver


def teardown_driver(driver):
    driver.quit()


def login_to_interia_poczta(driver, email, password):
    driver.get("https://poczta.interia.pl/logowanie/")
    try:
        rodo_agree_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
        rodo_agree_button.click()
    except:
        pass

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn--login").click()


def test_login_into_interia_poczta_success():
    driver = setup_driver()
    try:
        login_to_interia_poczta(
            driver, "code.brainers.tester@interia.pl", "testerZAQ!2wsx"
        )
        sleep(3)
        assert driver.title.startswith("Poczta w Interii")
    finally:
        teardown_driver(driver)


def test_login_into_interia_poczta_wrong_credentials():
    driver = setup_driver()
    try:
        login_to_interia_poczta(
            driver, "code.brainers.tester@interia.pl", "tester_not_existing"
        )
        sleep(3)
        error = driver.find_element(By.CLASS_NAME, "form__error")
        assert error.text.strip() == "Błędny e-mail lub hasło."
    finally:
        teardown_driver(driver)
