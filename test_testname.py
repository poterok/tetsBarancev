# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.action_chains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestname():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  


  name = 'Hello'


  def test_testname(self):
    self.driver.get("https://id.rambler.ru/login-20/login?back=https%3A%2F%2Fwww.rambler.ru&rname=head&type=self")
    time.sleep(1)

    self.driver.find_element_by_id("login").click()
    self.driver.find_element_by_id("login").send_keys("potr4ik")
    self.driver.find_element_by_id("password").clear()
    self.driver.find_element_by_id("password").send_keys("2012Potr")
    time.sleep(1)
    self.driver.find_element_by_css_selector('span.rui-Button-content').click()
    time.sleep(2)
    self.driver.find_element_by_css_selector('span.rui__1vTeO').click()
    time.sleep(2)

    # time.sleep(2)
    self.driver.find_element_by_css_selector('a.rui__iDgq5').click()
    time.sleep(1)
    self.driver.find_element_by_css_selector('#app > div.App-root-hg > div.AppContainer-root-3m.AutoAppContainer-root-2P > div.Header-root-2e.sc-bxivhb.hRHwcA > div > div.Header-main-jB > div.Header-headLinks-1F > div.tour__contacts-button > span > a > div > div > div > span:nth-child(2)').click()
    time.sleep(1)

    # Жмем еще
    self.driver.find_element_by_css_selector('#app > div.App-root-hg > div.AppContainer-root-3m.AutoAppContainer-root-2P > div.AutoAppContainer-inner-1B > div.AutoAppContainer-sidebar-LW > div > div > div > div.Sidebar-content-1p.sc-bdVaJa.dWoGOq > div > div > li > div > div > div > span:nth-child(1)').click()

    # Создаем новую группу
    self.driver.find_element_by_css_selector('#app > div.App-root-hg > div.AppContainer-root-3m.AutoAppContainer-root-2P > div.AutoAppContainer-inner-1B > div.AutoAppContainer-sidebar-LW > div > div > div > div.Sidebar-content-1p.sc-bdVaJa.dWoGOq > div > a > span:nth-child(2)').click()

    # Ищем инпут Водим навание новой группы
    self.driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div > div > div.Group-group-qo > form > div.Input-root-35.Input-underlined-1I > div > input').send_keys(name + 'rwerwr')

    #Сохраняем
    self.driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div > div > div.Group-group-qo > form > div.Group-action-2M > button > span').click()



  def teardown_method(self, method):
    self.driver.quit()