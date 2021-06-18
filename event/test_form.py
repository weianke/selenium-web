from time import sleep

import pytest
from selenium import webdriver


class TestFrom():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_from(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys('123')
        self.driver.find_element_by_id("user_password").send_keys('password')
        # self.driver.find_element_by_id("user_remember_me").click()
        element1 = self.driver.find_element_by_css_selector('#user_remember_me')
        self.driver.execute_script("arguments[0].click();", element1)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(6)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_form.py'])