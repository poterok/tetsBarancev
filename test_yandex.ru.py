# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.action_chains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys




class TestYandex():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_1(self):
        driver = self.driver
        driver.get("https://yandex.ru")


    def teardown_method(self, method):
        self.driver.quit()



    def open_site(self, driver):
        driver.get("https://yandex.ru")
