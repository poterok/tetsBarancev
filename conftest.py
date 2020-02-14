from fixture.application import Application
from model.auth import Auth
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.open_site()
        fixture.session.login(Auth(username='poterok', password='Mnata1991'))
    else:
        if not fixture.valid():
            fixture = Application()
            fixture.open_site()
            fixture.session.login(Auth(username='poterok', password='Mnata1991'))
    return fixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.open_site()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture