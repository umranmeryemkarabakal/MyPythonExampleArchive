from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com")
#time.sleep(2)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q"))) # max 4 sn bekle
input_element_by_name = driver.find_element(By.NAME, "q")
# input_element_by_class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
time.sleep(2)

# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea

print(input_element_by_name)
# print(input_element_by_class_name)
# print(input_element_xpath)

input_element_by_name.send_keys("ümran meryem karabakal")
# time.sleep(2)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))
search_button = driver.find_element(By.NAME, "btnK")
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()






while True:
    continue

