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
    expected_title = "CodeBrainers – Prawdopodobnie najlepszy bootcamp w Polsce!"
    website_title = get_website_title(url)
    assert expected_title == website_title

test_codebrainers_title()
