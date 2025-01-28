from selenium import webdriver

def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def test_google_title():
    site_title = get_website_title(url="https://google.com/")
    assert site_title == "Google"

def test_codebrainers_title():
    url = "https://codebrainers.pl/"
    expected_title = "Coś więcej niż kodowanie - codebrainers"
    website_title = get_website_title(url)
    assert expected_title == website_title

def test_spidersweb_title():
    url = "https://spidersweb.pl/"
    expected_title = "Spider’s Web"
    website_title = get_website_title(url)
    assert expected_title == website_title