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
        self.app.driver.find_element_by_class_name('mail-LabelList').find_element_by_class_name('_nb-button-content').click()
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




        # Если уже есть группа и нужно создать еще

    def if_has_other_group(self, group_name):

        # Кнопка "Создать группу "
        try:
            # a = self.app.driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[2]/div[3]/div/div[1]/div/div/div[3]/div/div[2]/button/span/span')
            s = WebDriverWait(self.app.driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[2]/div[3]/div/div[1]/div/div/div[3]/div/div[2]/button/span/span')))
        except:
            s = None
        print(s)
        if s is None:
            # self.app.driver.find_element_by_link_text(group_name.name).click()
            self.app.driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[6]/div/div[3]/div[2]/div[3]/div/div[1]/div/div/div[4]/span').click()
            time.sleep(1)
            # Ввести название новой группы
            self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name(
                'mail-AbookPopup-Right').find_element_by_class_name('nb-input').send_keys(group_name.name)
            time.sleep(1)

            # Сохранить название группы
            self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name(
                'mail-AbookPopup-Selected-Buttons').find_element_by_css_selector('button.nb-button').click()
            time.sleep(1)
        else:
            #  'Создать группу'
            self.app.driver.find_element_by_class_name('mail-LabelList').find_element_by_class_name(
                '_nb-button-content').click()
            time.sleep(1)

            # Ввести название новой группы
            self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name(
                'mail-AbookPopup-Right').find_element_by_class_name('nb-input').send_keys(group_name.name)
            time.sleep(1)

            # Сохранить название группы
            self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name(
                'mail-AbookPopup-Selected-Buttons').find_element_by_css_selector('button.nb-button').click()
            time.sleep(1)

