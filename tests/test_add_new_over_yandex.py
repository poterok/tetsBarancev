# coding=utf-8
# Generated by Selenium IDE
import time
from model.auth import Auth
from model.named_group import Group
class GroupHelper:

    def __init__(self,app):
        self.app = app


def test_4_create_new_group_over(app):
    # app.open_site()
    # app.session.login(Auth(username='poterok', password='Mnata1991'))
    app.group.go_to_contacts()
    time.sleep(2)
    app.group.create_delete_group(Group(name='new wew'))
    # app.session.logout()
