from time import sleep

import pytest

from selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        self.driver.switch_to.parent_frame()
        # 还可以使用：切换为默认页面的方法
        # self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(5)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_frame.py'])