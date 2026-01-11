from selenium import webdriver

def test_onet_title():
    driver = webdriver.Chrome()
    driver.get("https://onet.pl/")
    print(driver.title)
    assert driver.title == "Onet – Jesteś na bieżąco"
    driver.quit()

# Ćwiczenie