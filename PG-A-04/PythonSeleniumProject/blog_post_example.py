from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://atilsamancioglu.com")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))

blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))

"""
read_buttons = driver.find_elements(By.CLASS_NAME, "button")
for button in read_buttons:
    print(button)
"""

read_button = driver.find_element(By.CLASS_NAME, "button")
read_button.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")))

article_list = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")
print(len(article_list.text.splitlines()))









while True:
    continue