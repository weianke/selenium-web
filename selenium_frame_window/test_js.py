from time import sleep

import pytest

from selenium_frame_window.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium 测试')
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        for code in[
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        time_element = self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_js.py'])