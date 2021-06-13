#!/usr/bin/env python
from selenium import webdriver

class TestHogWards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待5秒
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("http://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_css_selector(".topic-22621.title > a").click()