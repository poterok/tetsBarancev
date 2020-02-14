
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

import time


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def valid(self):
        try:
            self.driver.current_url
            return  True
        except:
            return False


    def open_site(self):
        self.driver.get("https://yandex.ru")



    def destroy(self):
        self.driver.quit()
