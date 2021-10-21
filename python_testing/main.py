import requests


def create_session():
    s = requests.Session()
    return s


def get_request(session, url):
    r = session.get(url)
    return r
