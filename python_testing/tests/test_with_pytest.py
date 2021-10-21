import pytest

from main import get_request


def test_google(session):
    r = get_request(session, "https://www.google.com")
    assert r.status_code == 200
    assert len(r.history) == 0


def test_google_redirect(session):
    r = get_request(session, "https://google.com")
    assert r.status_code == 200
    assert len(r.history) != 0


@pytest.mark.xfail
def test_wrong_url(session):
    r = get_request(session, "https://googles.com")
    r.raise_for_status()


@pytest.mark.parametrize(
    "url, status_code, len_history", [
        ("https://www.google.com", 200, 0),
        ("https://google.com", 200, 1)
    ]
)
def test_parameterize(url, status_code, len_history, session):
    r = get_request(session, url)
    assert r.status_code == status_code
    assert len(r.history) == len_history
