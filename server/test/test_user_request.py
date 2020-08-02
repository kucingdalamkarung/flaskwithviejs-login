import unittest
from app import create_app
from models.models import UserModel


class UserRequestTest(unittest.TestCase):
    app = create_app().test_client()

    def test_hello(self):
        res = self.app.get('/api/hello')
        self.assertEqual(res.status_code, 200)

    def test_user_main(self):
        res = self.app.get('/api/user')
        self.assertEqual(res.status_code, 200)
