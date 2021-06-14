from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id("su")
        el.send_keys('selenium 测试')
        action = TouchActions(self.driver)
        action.tap(el_search)
        # 搜索后滑动到底部
        action.scroll_from_element(el, 0, 10000).perform()
        # sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_TouchAction.py'])
