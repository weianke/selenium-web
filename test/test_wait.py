from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com")

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的主题"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, '//*[class="table-heading"]'))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()