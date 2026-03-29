from selenium import webdriver
from time import sleep

def test_onet_title():
    driver = webdriver.Safari()
    sleep(3)
    driver.get("https://onet.pl")
    sleep(3)
    print(driver.title)
    assert driver.title == "Onet – Jesteś na bieżąco"
    driver.quit()


def test_title_test_google():
    url ="https://www.google.com/"
    driver = webdriver.Safari()
    driver.get(url)
    assert driver.title == "Google"
    driver.quit()


def test_apple_title():
    driver = webdriver.Safari()
    sleep(3)
    driver.get("http://www.apple.com")
    sleep(3)
    print(driver.title)
    assert "Apple" in driver.title
    driver.quit()


def test_foundry_title():
    driver = webdriver.Safari()
    sleep(3)
    driver.get("https://foundryvtt.com/")
    sleep(5)
    print(driver.title)
    assert driver.title == "Home | Foundry Virtual Tabletop"
    driver.quit()
