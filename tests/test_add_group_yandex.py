# coding=utf-8
# Generated by Selenium IDE
from model.auth import Auth
from model.named_group import Group


def test_2_create_new_group(app):
    # app.open_site()
    # app.session.login(Auth(username='poterok', password='Mnata1991'))
    app.group.go_to_contacts()
    app.group.create_delete_group(Group(name='new wew'))
    # app.session.logout()
