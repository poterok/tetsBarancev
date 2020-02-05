import time

class GroupHelper:

    def __init__(self,app):
        self.app = app


def test_2_create_new_group(app):
    app.open_site()
    app.session.login(Auth(username='poterok', password='Mnata1991'))
    app.group.go_to_contacts()

    app.group.if_has_other_group(Group(name='new wew'))
    app.session.logout()
