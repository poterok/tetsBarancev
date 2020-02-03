import time

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, group_auth):
        self.app.driver.find_element_by_link_text('Войти в почту').click()
        time.sleep(1)
        self.app.driver.find_element_by_name('login').send_keys(group_auth.username)
        time.sleep(1)
        self.app.driver.find_element_by_class_name('passp-flex-wrapper')
        time.sleep(1)
        self.app.driver.find_element_by_class_name('button2_type_submit').click()
        time.sleep(1)
        self.app.driver.find_element_by_id('passp-field-passwd').send_keys(group_auth.password)
        time.sleep(1)
        # Подтвердить
        self.app.driver.find_element_by_class_name('button2_type_submit').click()
        time.sleep(3)



    def logout(self):
        time.sleep(1)
        self.app.driver.find_element_by_css_selector('div.mail-User-Name').click()
        time.sleep(1)
        self.app.driver.find_element_by_css_selector('div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front._nb-popup-outer.ui-dialog-no-close._nb-popup_to_bottom').find_element_by_link_text('Выйти из сервисов Яндекса').click()
        time.sleep(2)

