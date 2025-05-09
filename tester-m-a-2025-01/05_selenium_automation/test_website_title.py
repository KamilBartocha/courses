from selenium import webdriver

def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def test_codebrainers_title():
    url = "https://codebrainers.pl/"
    expected_title = "Coś więcej niż kodowanie - codrainers"
    website_title = get_website_title(url)
    assert expected_title == website_title

def test_google_title():
    url = "https://google.com/"
    expected_title = "Google"
    website_title = get_website_title(url)
    assert expected_title == website_title