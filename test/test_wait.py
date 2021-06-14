import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com")
        self.driver.maximize_window()

    def test_wait(self):
        # self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的主题"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="ember36"]')))
        self.driver.find_element(By.XPATH, '//*[@id="ember36"]').click()

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_wait.py'])