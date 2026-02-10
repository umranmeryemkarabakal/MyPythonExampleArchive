import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_in_unicornitems_com(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))  # max 4 sn bekle

        input_login_username = driver.find_element(By.NAME, "username")
        input_login_username.send_keys("meryem")

        input_login_password = driver.find_element(By.NAME, "password")
        input_login_password.send_keys(34)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul/li")))

        alert_message = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul/li")
        print(f"Hata mesajı içeriği: '{alert_message.text}'")
        assert "ERROR: " in alert_message.text

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
