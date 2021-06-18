from time import sleep

import pytest

from selenium_frame_window.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com')
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        sleep(3)
        self.driver.find_element_by_id('stfile').send_keys('/Users/anke/Downloads/avatar.jpeg')
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_file.py'])
