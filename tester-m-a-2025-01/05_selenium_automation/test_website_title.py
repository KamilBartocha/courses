from selenium import webdriver
from time import sleep

def get_website_title(url):
    driver = webdriver.Safari()
    driver.get(url)
    sleep(2)
    site_title = driver.title
    driver.quit()
    return site_title


def test_website_codebrainers():
    title = get_website_title(url="https://codebrainers.pl/")
    expected = "Coś więcej niż kodowanie - codebrainers"
    assert title == expected

def test_website_wp():
    assert get_website_title("https://www.wp.pl") == "Wirtualna Polska - Wszystko co ważne - www.wp.pl"

# def test_website_allegro1():
#     title = get_website_title(url="https://allegro.pl/")
#     expected = "Allegro - atrakcyjne ceny - Strona Główna"
#     assert title == expected

# def test_website_allegro2():
#     assert get_website_title(url="https://allegro.pl/") == "Allegro - atrakcyjne ceny - Strona Główna"

def test_website_quantum():
    title = get_website_title(url="https://quantum-software.com/en/")
    expected = "Quantum Qguar – IT systems for logistics"
    assert title == expected

def test_website_pudelek():
    title = get_website_title(url='https://www.pudelek.pl/')
    expected = "Pudelek.pl - Plotki, Gwiazdy, Sensacja - Pudelek"
    assert title == expected

def test_website_google():
    assert get_website_title("https://www.google.pl/") == "Google"

def test_website_interia():
    """Interia - Polska i świat: informacje, sport, gwiazdy."""
    assert get_website_title("https://www.interia.pl") == "Interia - Polska i świat: informacje, sport, gwiazdy."
