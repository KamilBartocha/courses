# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep

def test_bing_search_success():
    """
    GIVEN "selenium alamakota" is typed into search on site bing.com
    WHEN "ENTER" is pressed (search request)
    THEN Result stats are calculated and visible on screen
    """
    pass

def test_bing_search_link_into_selenium():
    """
    GIVEN "selenium" is typed into search on site bing.com
    AND "ENTER" is pressed (search request)
    AND "selenium.dev" hyperlink is found
    WHEN link is clicked
    THEN selenium.dev website is loaded
    """
    pass


def test_selenium_documentation_link():
    """
    GIVEN https://www.selenium.dev/ is opened
    AND Documentation link is found
    WHEN link is clicked
    THEN selenium.dev/documentation website is loaded

    wskazówka: By.LINK_TEXT, "Documentation"
    """
    pass
