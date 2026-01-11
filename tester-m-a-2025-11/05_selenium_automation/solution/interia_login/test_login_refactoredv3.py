"""
- ładowanie zmiennych z loginem/hasłem z pliku .env
- driver w @pytest.fixture
- explicit waits z EC.
- dekorator @pytest.mark.login w testach loginu
czas: 9sec
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv


load_dotenv()  # vars from .env file

INTERIA_LOGIN_URL = "https://poczta.interia.pl/logowanie/"


@pytest.fixture
def driver():
    driver = webdriver.Safari()
    yield driver
    driver.quit()


def login_to_interia_poczta(driver, email, password):
    driver.get(INTERIA_LOGIN_URL)

    try:
        rodo_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "rodo-popup-agree"))
        )
        rodo_button.click()
    except TimeoutException:
        pass

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn--login").click()


@pytest.mark.login
def test_login_success(driver):
    email = os.getenv("INTERIA_EMAIL")
    password = os.getenv("INTERIA_PASSWORD")

    assert email and password, "Credentials must be set in the .env file."

    login_to_interia_poczta(driver, email, password)

    WebDriverWait(driver, 10).until(EC.title_is("Poczta w Interii"))
    assert driver.title == "Poczta w Interii"


@pytest.mark.login
def test_login_wrong_credentials(driver):
    email = os.getenv("INTERIA_EMAIL")
    wrong_password = "wrongPassword123!"

    login_to_interia_poczta(driver, email, wrong_password)

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "form__error"))
    )
    assert error.text.strip() == "Błędny e-mail lub hasło."
