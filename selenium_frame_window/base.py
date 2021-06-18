import os

from selenium import webdriver


class Base():
    def setup(self):
        brower = os.getenv('browser')
        if brower == 'firefox':
            self.driver = webdriver.Firefox()
        elif brower == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()