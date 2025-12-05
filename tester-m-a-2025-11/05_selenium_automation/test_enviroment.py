from selenium import webdriver
from time import sleep

def test_onet_title():
    driver = webdriver.Safari()
    driver.get("https://onet.pl/")
    site_title = driver.title
    sleep(3)
    driver.quit()
    expected_title = "Onet – Jesteś na bieżąco"  #<html> -> <head><title>xxxxx</title></head>
    assert expected_title == site_title
