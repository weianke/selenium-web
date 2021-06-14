from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_dobuleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_dobuleclick)
        action.perform()

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_actionChains.py'])
