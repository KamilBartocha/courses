from selenium import webdriver
from time import sleep

def test_title_codebrainers():
    driver = webdriver.Safari()
    driver.get("https://codebrainers.pl/")
    site_title = driver.title
    expected_title = "Coś więcej niż kodowanie - codebrainers"
    assert site_title == expected_title
    driver.quit()

def test_title_allegro():
    driver = webdriver.Safari()
    driver.get("https://allegro.pl/")
    site_title = driver.title
    print(site_title)
    expected_title = "allegro.pl"
    assert site_title == expected_title
    driver.quit()

def test_title_sinthome():
    driver = webdriver.Safari()
    driver.get("https://sinthome.pl/")
    site_title = driver.title
    expectes_title = "strona główna - Sinthome"
    assert site_title == expectes_title
    driver.quit()

def test_title_wloszczowa():
    driver = webdriver.Safari()
    driver.get("https://wloszczowa.pl/")
    site_title = driver.title
    print(site_title)
    expected_title = "Portal informacyjny Gminy Włoszczowa - UG Włoszczowa"
    assert site_title == expected_title
    driver.quit()

def test_Selenium_TITLE():
    driver = webdriver.Safari()
    driver.get("https://selenium-python.readthedocs.io/index.html")
    site_title = driver.title
    print(site_title)
    assert site_title == "Selenium with Python — Selenium Python Bindings 2 documentation"
    driver.quit() # zamyka całą

def test_title_wirtualna_polska():
    driver = webdriver.Safari()
    driver.get("https://www.wp.pl/")
    site_title = driver.title
    expected_title = "Wirtualna Polska - Wszystko co ważne - www.wp.pl"
    assert site_title == expected_title
    driver.quit()

def test_title_Pudelek():
    driver = webdriver.Safari()
    driver.get("https://www.pudelek.pl/")
    site_title = driver.title
    print(site_title)
    assert site_title == "Pudelek.pl - Plotki, Gwiazdy, Sensacja - Pudelek"
    sleep(5) # Czekaj 5 sekund
    driver.quit()


