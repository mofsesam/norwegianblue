import os
import tempfile

import pytest

from .. import DemoMicroservice

# https://flask.palletsprojects.com/en/1.1.x/testing/
# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

@pytest.fixture(scope='module')
def client():
    db_fd, DemoMicroservice.app.config['DATABASE'] = tempfile.mkstemp()
    DemoMicroservice.app.config['TESTING'] = True

    with DemoMicroservice.app.test_client() as client:
        with DemoMicroservice.app.app_context():
            pass
        yield client

    os.close(db_fd)
    os.unlink(DemoMicroservice.app.config['DATABASE'])

@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('MY_SETTING', 'some-value')
    monkeypatch.setenv('ANOTHER_SETTING', 'some-value')
