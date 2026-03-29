from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_bing_search_success():
    """
    GIVEN "selenium alamakota" is typed into search on site bing.com
    WHEN "ENTER" is pressed (search request)
    THEN Result stats are calculated and visible on screen
    """
    driver = webdriver.Safari()
    driver.get("https://www.bing.com/")
    search = driver.find_element(By.ID, "sb_form_q")
    sleep(3)
    search.click()
    search.send_keys("selenium alamakota")
    search.send_keys(Keys.ENTER)
    sleep(3)
    results = driver.find_element(By.CLASS_NAME, "sb_count")
    print(results.text)  # About 36,700 results   # można regexp import re
    assert results.text.startswith("About")
    sleep(3)
    driver.quit()


def test_bing_search_link_into_selenium():
    """
    GIVEN "selenium" is typed into search on site bing.com
    AND "ENTER" is pressed (search request)
    AND "selenium.dev" hyperlink is found
    WHEN link is clicked
    THEN selenium.dev website is loaded
    """

    driver = webdriver.Safari()
    driver.get("https://www.bing.com/")
    search = driver.find_element(By.ID, "sb_form_q")
    sleep(3)
    search.click()
    search.send_keys("selenium")
    search.send_keys(Keys.ENTER)
    sleep(3)
    selenium_link = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium.dev")
    selenium_link.click()
    sleep(3)
    print(driver.title)
    driver.quit()


def test_selenium_documentation_link():
    """
    GIVEN https://www.selenium.dev/ is opened
    AND Documentation link is found
    WHEN link is clicked
    THEN selenium.dev/documentation website is loaded

    wskazówka: By.LINK_TEXT, "Documentation"
    """
    driver = webdriver.Safari()
    driver.maximize_window()  # lub driver.set_window_size(1920, 1080)
    driver.get("https://www.selenium.dev/")
    sleep(5)
    selenium_link = driver.find_element(By.LINK_TEXT, "Documentation")
    selenium_link.click()
    sleep(3)
    print(driver.title)
    assert "The Selenium Browser Automation Project | Selenium" == driver.title
    driver.quit()


def test_bing_search_implicit():
    driver = webdriver.Safari()
    driver.implicitly_wait(10)

    driver.get("https://www.bing.com/")

    # Driver will poll up to 10s
    search = driver.find_element(By.ID, "sb_form_q")
    search.click()
    search.send_keys("selenium")
    search.send_keys(Keys.ENTER)

    # Driver will poll up to 10s
    selenium_link = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium.dev")
    selenium_link.click()

    print(driver.title)

    driver.quit()


def test_bing_search_explicit():
    driver = webdriver.Safari()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.bing.com/")
        search = wait.until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
        search.click()
        search.send_keys("selenium")
        search.send_keys(Keys.ENTER)

        selenium_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "selenium.dev")))
        selenium_link.click()

        wait.until(EC.url_contains("selenium.dev"))
        print(driver.title)
    finally:
        driver.quit()