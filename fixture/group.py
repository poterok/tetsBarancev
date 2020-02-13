import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GroupHelper:

    def __init__(self,app):
        self.app = app


    def go_to_contacts(self):
        self.app.driver.find_element_by_link_text('Контакты').click()
        time.sleep(2)

    def create_new_group(self, group_name):
        # Создать группу
        # self.app.driver.find_element_by_class_name('mail-LabelList').find_element_by_class_name('_nb-button-content').click()
        self.app.driver.find_element_by_css_selector('div.mail-Layout-Aside-Inner').find_element_by_css_selector('div.ns-view-abook-left-box').find_element_by_css_selector('div.ns-view-abook-left').find_element_by_css_selector('span._nb-button-text').click()
        time.sleep(1)

        # Ввести название новой группы
        self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Right').find_element_by_class_name('nb-input').send_keys(group_name.name)
        time.sleep(1)

        # Сохранить название группы
        self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Selected-Buttons').find_element_by_css_selector('button.nb-button').click()
        time.sleep(1)

    def go_to_new_group(self, group_name):
        # Перейти в группу
        self.app.driver.find_element_by_link_text(group_name.name).click()
        time.sleep(2)

    def go_to_settings_group(self):
        # # Перейти в настройки групп
        self.app.driver.find_element_by_class_name('mail-LabelList-Setup').find_element_by_link_text('настроить…').click()
        time.sleep(3)

    def choose_group_for_delete(self):
        # # Выбрать группу для удаления
        self.app.driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[3]/div[2]/div[5]/div/div/div[2]/div[2]/ul/li[3]/span[2]').click()
        time.sleep(2)

    def delete_group(self):
        # # Удалить группу
        self.app.driver.find_element_by_xpath('//*[@id="nb-12"]/span/span/span').click()




        # Если уже есть группа то удк

    def create_delete_group(self, group_name):
        try:
            self.app.driver.find_element_by_css_selector('div.mail-Layout-Aside-Inner').find_element_by_css_selector('div.ns-view-abook-left-box').find_element_by_css_selector('div.ns-view-abook-left').find_element_by_css_selector('span._nb-button-text')
            print('Кнопка "Создать группу" есть')
            self.create_new_group(group_name)
            print('1')
        except:
            self.app.driver.find_element_by_css_selector('div.mail-Layout-Aside-Inner').find_element_by_css_selector('div.ns-view-abook-left-box').find_element_by_css_selector('div.mail-LabelList-Setup').find_element_by_css_selector('a.mail-LabelList-Setup_link').click()
            time.sleep(1)
            self.app.driver.find_element_by_css_selector('div.setup-abook-groups').find_element_by_css_selector('ul.setup-abook-groups__inner').find_element_by_css_selector('li.setup-abook-group_editable').click()
            # Нажать кнопку Удалить (в списке 3)
            self.app.driver.find_element_by_xpath("//div[@class='setup-abook-groups-actions']/button[3]").click()
            print('Удалил нахер')
