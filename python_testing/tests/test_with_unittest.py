from unittest import TestCase

from main import create_session, get_request


class Testing(TestCase):
    def setUp(self):
        self.s = create_session()

    def test_google(self):
        r = get_request(self.s, "https://www.google.com")
        self.assertIs(r.status_code, 200)
        self.assertIs(len(r.history), 0)

    def test_google_redirect(self):
        r = get_request(self.s, "https://google.com")
        self.assertIs(r.status_code, 200)
        self.assertIsNot(r.history, [])

    def test_always_failed(self):
        self.assertTrue(False, 'This test case is expected to be failed')

    def tearDown(self):
        self.s.close()
