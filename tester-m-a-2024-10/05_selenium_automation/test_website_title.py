from selenium import webdriver
from time import sleep

def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def test_codebrainers_title():
    url = "https://codebrainers.pl/"
    expected_title = "Coś więcej niż kodowanie - codebrainers"
    website_title = get_website_title(url)
    assert expected_title == website_title

def test_google_title():
    url = "https://google.com/"
    expected_title = "Google"
    website_title = get_website_title(url)
    assert expected_title == website_title

def test_cb_kontakt():
    url = "https://codebrainers.pl/kontakt"
    excepted_title = "Kontakt | CodeBrainers.pl - codebrainers"
    website_title = get_website_title(url)
    assert website_title == excepted_title
