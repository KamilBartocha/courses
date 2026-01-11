# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep


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
    pass

def test_interia_login_wrong_cred():
    """
    Test Scenario:

    GIVEN poczta.interia.pl/logowanie is loaded
        AND unregistered user credentials are typed into login form
    WHEN "Zaloguj się" button is pressed (log request)
    THEN User is not logged in and error is present
    """
    pass
