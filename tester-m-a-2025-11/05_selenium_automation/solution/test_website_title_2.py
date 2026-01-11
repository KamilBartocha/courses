from selenium import webdriver

def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title

def test_onet_title():
    title = get_website_title("https://onet.pl/")
    assert title == "Onet – Jesteś na bieżąco"
