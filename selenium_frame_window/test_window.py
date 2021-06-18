from time import sleep

import pytest

from selenium_frame_window.base import Base

class TestWindow(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # 切换页面到注册页面
        windows = self.driver.window_handles
        # 切换到最后一个窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('username')
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys('13509879908')
        sleep(2)
        # 回到登录页面，点击登录
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('189382784343')
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('0988')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_window.py'])

