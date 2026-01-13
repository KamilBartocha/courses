from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_bing_search_success():
    """
    GIVEN "selenium alamakota" is typed into search on site https://www.bing.com
    WHEN "ENTER" is pressed (search request)
    THEN Result stats are calculated and visible on screen
    """
    try:
        driver = webdriver.Safari()
        driver.get("https://www.bing.com")
        sleep(2)
        search_form = driver.find_element(By.ID, "sb_form_q")
        search_form.send_keys("selenium alamakota")
        search_form.send_keys(Keys.ENTER)
        sleep(4)
        results_count = driver.find_element(By.PARTIAL_LINK_TEXT, "sb_count")
        print(results_count.text)
        assert results_count.text.startswith("About") and results_count.text.endswith("results")
    finally:
        driver.quit()



def test_bing_search_link_into_selenium():
    """
    GIVEN "selenium" is typed into search on site https://www.bing.com
    AND "ENTER" is pressed (search request)
    AND "selenium.dev" hyperlink is found (By.LINK_TEXT, "link.dev") or (By.PARTIAL_LINK_TEXT, "selenium.dev")
    WHEN link is clicked
    THEN selenium.dev website is loaded (title can be used for verification)
    """
    try:
        url_bing = "https://www.bing.com"
        driver = webdriver.Safari()
        driver.implicitly_wait(10)
        driver.get(url_bing)
        original_window = driver.current_window_handle
        search_box = driver.find_element(By.ID,"sb_form_q")
        search_box.send_keys("Selenium")
        search_box.submit()
        sleep(3)
        print(driver.title)
        link_selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "selenium")
        link_selenium.click()
        sleep(3)
        for window_handle in driver.window_handles:   #change window(karta)
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        print(driver.title)
        assert "Selenium" == driver.title
    finally:
        driver.quit()


def test_selenium_documentation_link():
    """
    GIVEN https://www.selenium.dev/ is opened
    AND Documentation link is  (By.LINK_TEXT, "Documentation")
    WHEN link is clicked
    THEN selenium.dev/documentation website is loaded

    wskazówka: By.LINK_TEXT, "Documentation"
    """
    try:
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.selenium.dev/")

        documentation = driver.find_element(By.LINK_TEXT, "Documentation")
        documentation.click()

        sleep(5)
        print(driver.title)
        assert driver.title == "The Selenium Browser Automation Project | Selenium"
    finally:
        driver.quit()
