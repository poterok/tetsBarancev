from fixture.application import Application
from model.auth import Auth
import pytest


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.open_site()
    fixture.session.login(Auth(username='poterok', password='Mnata1991'))
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture