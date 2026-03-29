from selenium import webdriver
from time import sleep
# def test_onet_title_tmp():
#     actual_title = get_website_title("https://onet.pl")
#     expected_title = "Onet – Jesteś na bieżąco"
#     assert actual_title == expected_title


def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title


def test_onet_title():
    assert get_website_title("https://onet.pl") == "Onet – Jesteś na bieżąco"


def test_title_test_google():
    assert get_website_title("https://www.google.com/") == "Google"


def test_apple_title():
    assert get_website_title("https://www.apple.com/") == "Apple"


def test_foundry_title():
    assert get_website_title("https://www.foundryvtt.com/") == "Home | Foundry Virtual Tabletop"
