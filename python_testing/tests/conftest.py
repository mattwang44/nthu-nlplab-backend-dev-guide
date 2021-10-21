
import pytest

from main import create_session


@pytest.fixture(scope='function')
def session():
    s = create_session()
    yield s
    s.close()
