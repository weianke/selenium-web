from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_dobuleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_dobuleclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        # ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        # 动作最终执行需要调用的方法
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # 两种写法，第一种拖拽
        # action.drag_and_drop(drag_element, drop_element).perform()
        # 第二种拖拽
        # action.click_and_hold(drag_element).release(drop_element).perform()
        # 第三张拖拽
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm");
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACKSPACE).perform()

        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_actionChains.py'])
