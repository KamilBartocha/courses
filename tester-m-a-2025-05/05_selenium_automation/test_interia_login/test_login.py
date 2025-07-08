from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_login_into_interia_poczta():
    """
        przed zalogowaniem się title:Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta
        po zalogowaniu się title:Poczta w Interii
    """

    driver = webdriver.Safari()
    driver.get("https://poczta.interia.pl/logowanie/")
    sleep(3)

    rodo_agree_button = driver.find_element(By.CLASS_NAME, "rodo-popup-agree") #class="rodo-popup-agree"
    rodo_agree_button.click()


    email_form = driver.find_element(By.ID, "email")  #id="email"
    email_form.click()
    email_form.send_keys("code.brainers.tester@interia.pl")

    pass_form = driver.find_element(By.ID, "password")  # id="password"
    pass_form.click()
    pass_form.send_keys("testerZAQ!2wsx")

    login_button = driver.find_element(By.CLASS_NAME, "btn--login")  #class="btn btn--login btn"

    print(driver.title)
    assert driver.title == "Poczta w Interia.pl - darmowa poczta e-mail – logowanie do konta"
    login_button.click()
    sleep(3)
    print(driver.title)
    assert driver.title == "Poczta w Interii"
    sleep(5)
    driver.quit()