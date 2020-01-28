# coding=utf-8
# Generated by Selenium IDE
from selenium import webdriver
import time


class TestYandex():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_1_delete_group(self):
        self.open_site()
        self.login()
        self.go_to_contacts()
        self.go_to_new_group()
        self.go_to_settings_group()
        self.choose_group_for_delete()
        self.delete_group()
        self.open_site()


    def test_2_create_new_group(self):
        self.open_site()
        self.login()
        self.go_to_contacts()
        self.create_new_group()
        self.open_site()



    def teardown_method(self, method):
        self.driver.quit()



# Функции


    def open_site(self):
        self.driver.get("https://yandex.ru")

    def login(self):
        self.driver.find_element_by_link_text('Войти в почту').click()
        time.sleep(1)
        self.driver.find_element_by_name('login').send_keys('poterok')
        time.sleep(1)
        self.driver.find_element_by_class_name('passp-flex-wrapper')
        time.sleep(1)
        self.driver.find_element_by_class_name('button2_type_submit').click()
        time.sleep(1)
        self.driver.find_element_by_id('passp-field-passwd').send_keys('Mnata1991')
        time.sleep(1)
        self.driver.find_element_by_class_name('button2_type_submit').click()
        time.sleep(3)

        # Привязка номера ?
        # self.driver.find_element_by_css_selector('div.passp-auth')
        # self.driver.find_element_by_css_selector('div.passp-auth-content')
        # self.driver.find_element_by_class_name('passp-route-forward')
        # self.driver.find_element_by_class_name('passp-route-enter-done')
        # time.sleep(3)
    def go_to_contacts(self):
        self.driver.find_element_by_link_text('Контакты').click()
        time.sleep(2)

    def create_new_group(self):
        # Создать группу
        self.driver.find_element_by_class_name('mail-LabelList').find_element_by_class_name('_nb-button-content').click()
        time.sleep(1)

        # Ввести название новой группы
        self.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Right').find_element_by_class_name('nb-input').send_keys('Новая группа')
        time.sleep(1)

        # Сохранить название группы
        self.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Selected-Buttons').find_element_by_css_selector('button.nb-button').click()
        time.sleep(1)

    def go_to_new_group(self):
        # Перейти в группу
        self.driver.find_element_by_link_text('Новая группа').click()
        time.sleep(2)

    def go_to_settings_group(self):
        # # Перейти в настройки групп
        self.driver.find_element_by_class_name('mail-LabelList-Setup').find_element_by_link_text('настроить…').click()
        time.sleep(3)

    def choose_group_for_delete(self):
        # # Выбрать группу для удаления
        self.driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[3]/div[2]/div[5]/div/div/div[2]/div[2]/ul/li[3]/span[2]').click()
        time.sleep(2)

    def delete_group(self):
        # # Удалить группу
        self.driver.find_element_by_xpath('//*[@id="nb-12"]/span/span/span').click()
        time.sleep(3)
