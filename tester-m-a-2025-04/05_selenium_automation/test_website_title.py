from selenium import webdriver
from time import sleep

def test_title_onet_pl():
    driver = webdriver.Safari()
    driver.get("https://onet.pl/")
    sleep(5)
    site_title = driver.title
    print(site_title)
    assert site_title == "Onet – Jesteś na bieżąco"
    driver.quit()

def test_title_naszosie_pl():
    driver = webdriver.Safari()
    driver.get("https://naszosie.pl")
    sleep(1)
    site_title = driver.title
    print(site_title)
    assert site_title == "naszosie.pl"
    sleep(5) #czeka 5s
    driver.quit()

def test_title_me_pl():
    driver = webdriver.Safari()
    print(driver)
    sleep(2)
    driver.get("https://mediaexpert.pl")
    sleep(2)
    site_title = driver.title
    assert site_title == "Media Expert | Sklep internetowy RTV, AGD, komputery"
    sleep(2)
    driver.quit()

def test_title_mrbuggy_pl():
    driver = webdriver.Safari()
    driver.get("http://mrbuggy.pl/")
    sleep(5)
    site_title = driver.title
    print(site_title)
    assert site_title == "Mr Buggy"
    driver.quit()

## sposób 2
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