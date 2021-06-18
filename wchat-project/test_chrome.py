from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestChrome():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222/"
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get('https://home.testing-studio.com/')
        self.driver.find_element_by_link_text('所有分类').click()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_chrome.py'])