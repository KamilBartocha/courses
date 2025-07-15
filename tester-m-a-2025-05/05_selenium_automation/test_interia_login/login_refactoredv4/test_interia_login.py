"""
- ładowanie zmiennych z loginem/hasłęm z pliku .env
- driver w @pytest.fixture
- explicit waits z EC.
- dekorator @pytest.mark.login w testach loginu
- dodanie zapisywanie screenshot jeśli test failed -> conftest.py
- POM, pages z lokatorami danej strony.
czas: 9sec
"""


import os
import pytest
from datetime import datetime

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.interia_login_page import InteriaLoginPage

load_dotenv()

SCREENSHOT_DIR = "screenshots"

@pytest.fixture
def driver(request):
    driver = webdriver.Safari()
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.mark.login
def test_login_success(driver):
    email = os.getenv("INTERIA_EMAIL")
    password = os.getenv("INTERIA_PASSWORD")
    assert email and password, "Credentials must be set in the .env file."

    login_page = InteriaLoginPage(driver)
    login_page.login(email, password)

    WebDriverWait(driver, 10).until(EC.title_is("Poczta w Interii"))
    assert driver.title == "Poczta w"

@pytest.mark.login
def test_login_wrong_credentials(driver):
    email = os.getenv("INTERIA_EMAIL")
    wrong_password = "wrongPassword123!"

    login_page = InteriaLoginPage(driver)
    login_page.login(email, wrong_password)

    error_message = login_page.get_error_message()
    assert error_message == "Błędny e-mail lub hasło."
