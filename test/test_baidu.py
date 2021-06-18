from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Baidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        # sleep(2)
        self.driver.find_element_by_id('kw').send_keys('333')


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_baidu.py'])