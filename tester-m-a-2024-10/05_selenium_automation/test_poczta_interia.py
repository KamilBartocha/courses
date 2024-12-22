from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

def log_into_interia_poczta(user, password):
    driver = webdriver.Safari()
    driver.get("https://poczta.interia.pl/logowanie")
    print(f"title logowanie: {driver.title}")
    driver.implicitly_wait(3)

    # Akceptacja RODO
    go_to_service = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    go_to_service.click()
    sleep(3)


    # Wpisywanie nazwy e-mail
    input_email = driver.find_element(By.ID, "email")
    input_email.send_keys(user)
    sleep(3)


    # Wpisywanie hasła
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys(password)
    sleep(3)


    # Kliknięcie Zaloguj się
    button_log_in = driver.find_element(By.CLASS_NAME, "btn")
    button_log_in.click()
    sleep(5)

    print(f"Title zalogowany: {driver.title}")
    # assert driver.title == "Poczta w Interii"
    sleep(5)
    site_title = driver.title
    driver.quit()
    return site_title


def test_can_log_interia_email_valid_cred():
    actual_result = log_into_interia_poczta("code.brainers.tester@interia.pl",
                                            "testerZAQ!2wsx")
    except_result = "Poczta w Interii"
    assert actual_result.startswith(except_result)


def test_can_log_interia_email_invalid_cred():
    actual_result = log_into_interia_poczta("code.brainers.tester@interia.pl",
                                            "testerZAQ")
    assert actual_result.startswith("Poczta w Interia.pl")
