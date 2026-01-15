from selenium import webdriver
from selenium.webdriver.common.by import By
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
    code.brainers.tester@interia.pl
    tester
    """
    #GIVEN
    poczta_url = "https://poczta.interia.pl/logowanie"
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get(url=poczta_url)
    sleep(4)
    #<button class="rodo-popup-agree
    rodo_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    rodo_button.click()

    #AND
    form_user_email = driver.find_element(By.ID, "email")     #id="email"
    form_user_email.click()
    form_user_email.send_keys("code.brainers.tester@interia.pl")

    form_password = driver.find_element(By.ID, "password")    #id="password"
    form_password.click()
    form_password.send_keys("testerZAQ!2wsx")

    #WHEN
    login_button = driver.find_element(By.CLASS_NAME, "btn--login")
    print(driver.title)
    assert driver.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    login_button.click()

    #THEN
    sleep(6)
    print(driver.title)
    assert "Poczta w Interii" in driver.title
    driver.quit()




def test_interia_login_wrong_cred():
    """
    Test Scenario:

    GIVEN poczta.interia.pl/logowanie is loaded
        AND unregistered user credentials are typed into login form
    WHEN "Zaloguj się" button is pressed (log request)
    THEN User is not logged in
    AND error is present
    """
    #GIVEN
    poczta_url = "https://poczta.interia.pl/logowanie"
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get(url=poczta_url)
    sleep(4)

    rodo_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    rodo_button.click()
    sleep(3)
    #AND
    form_user_email = driver.find_element(By.ID, "email")     #id="email"
    form_user_email.click()
    form_user_email.send_keys("wrong_email_test@interia.pl")

    form_password = driver.find_element(By.ID, "password")    #id="password"
    form_password.click()
    form_password.send_keys("not_existing_password")

    #WHEN
    login_button = driver.find_element(By.CLASS_NAME, "btn--login")
    print(driver.title)
    assert driver.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    login_button.click()
    assert driver.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    sleep(4)
    # AND
    form_error = driver.find_element(By.CLASS_NAME, "form__error")
    assert form_error.text == "Błędny e-mail lub hasło."

    driver.quit()
