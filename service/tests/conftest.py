import os
import tempfile

import pytest

from .. import norwegianblue

# https://flask.palletsprojects.com/en/1.1.x/testing/
# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

@pytest.fixture(scope='module')
def client():
    db_fd, norwegianblue.app.config['DATABASE'] = tempfile.mkstemp()
    norwegianblue.app.config['TESTING'] = True

    with norwegianblue.app.test_client() as client:
        with norwegianblue.app.app_context():
            pass
        yield client

    os.close(db_fd)
    os.unlink(norwegianblue.app.config['DATABASE'])

@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('TESTING', "True")
    monkeypatch.setenv('DEBUG', "True")
