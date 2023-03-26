# import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_browser = webdriver.Chrome()

chrome_browser.get("https://kserdult.github.io/netflixcv/")

chrome_browser.find_element(
    By.CSS_SELECTOR, 'href="/netflixcv/assets/CV-ENG-b1ef38b4.pdf"'
)

print("All done press Enter to quit")
input = input()
