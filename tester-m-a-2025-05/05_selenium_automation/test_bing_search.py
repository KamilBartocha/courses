from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_search_bing():
    """
    GIVEN "test lorem ipsum lorem ipsum lorem ipsum" is typed into search on site bing.com
    WHEN "ENTER" is pressed (search request)
    THEN Result stats are calculated and visible on screen
    """
    driver = webdriver.Safari()
    driver.get("https://www.bing.com/")
    sleep(4)
    search_form = driver.find_element(By.ID, "sb_form_q") #id="sb_form_q"
    search_form.click()
    search_form.send_keys("test lorem ipsum lorem ipsum lorem ipsum ala ma kota")
    sleep(3)

    search_form.send_keys(Keys.ENTER)
    sleep(3)

    results = driver.find_element(By.ID, "b_tween_searchResults")  #b_tween_searchResults
    print(results)
    print(results.text)
    assert results.text.startswith("About")  #About 142,000 results
    sleep(3)
    driver.quit()
