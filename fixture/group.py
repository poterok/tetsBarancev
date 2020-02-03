import time

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
        self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Right').find_element_by_class_name('nb-input').send_keys(group_name)
        time.sleep(1)

        # Сохранить название группы
        self.app.driver.find_element_by_class_name('ui-dialog').find_element_by_class_name('mail-AbookPopup-Selected-Buttons').find_element_by_css_selector('button.nb-button').click()
        time.sleep(1)

    def go_to_new_group(self):
        # Перейти в группу
        self.app.driver.find_element_by_link_text('Новая группа').click()
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