from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_interia_login_correct_cred():
    """
    Test Scenario:

    GIVEN poczta.interia.pl/logowanie is loaded
        AND registered user credentials are typed into login form
    WHEN "Zaloguj się" button is pressed (log request)
    THEN User is logged in and email box is opened

    przed zalogowaniem się  title:Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta
    po zalogowaniu się      title:Poczta w Interii
    """
    d = webdriver.Safari()
    d.maximize_window()
    d.get("https://poczta.interia.pl/logowanie/")
    sleep(3)
    rodo_popup_agree = d.find_element(By.CLASS_NAME, "rodo-popup-agree") # class="rodo-popup-agree rodo-popup-main-agree"
    rodo_popup_agree.click()
    sleep(3)

    login_form = d.find_element(By.ID, "email")  #id="email"
    login_form.click()
    login_form.send_keys("code.brainers.tester@interia.pl")

    pass_from  = d.find_element(By.ID, "password")  # id="password"
    pass_from.click()
    pass_from.send_keys("testerZAQ!2wsx")


    assert d.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    login_button = d.find_element(By.CLASS_NAME, "btn--login")    #class="btn btn--login btn"
    login_button.click()
    sleep(5)
    assert d.title == "Poczta w Interii"
    d.quit()


def test_interia_login_wrong_cred():
    """
    Test Scenario:

    GIVEN poczta.interia.pl/logowanie is loaded
        AND unregistered user credentials are typed into login form
    WHEN "Zaloguj się" button is pressed (log request)
    THEN User is not logged in and error is present
    """
    d = webdriver.Safari()
    d.maximize_window()
    d.get("https://poczta.interia.pl/logowanie/")
    sleep(3)
    rodo_popup_agree = d.find_element(By.CLASS_NAME, "rodo-popup-agree") # class="rodo-popup-agree rodo-popup-main-agree"
    rodo_popup_agree.click()
    sleep(3)

    login_form = d.find_element(By.ID, "email")  #id="email"
    login_form.click()
    login_form.send_keys("code.brainers.tester@interia.pl")

    pass_from  = d.find_element(By.ID, "password")  # id="password"
    pass_from.click()
    pass_from.send_keys("tester_incorrect_password")

    login_button = d.find_element(By.CLASS_NAME, "btn--login")    #class="btn btn--login btn"
    login_button.click()
    sleep(5)
    form_error = d.find_element(By.CLASS_NAME, "form__error")
    assert form_error.text == "Błędny e-mail lub hasło."
    d.quit()