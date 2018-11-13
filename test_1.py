import unittest
import json
from first_flask_8 import app as test_app


class TestApp(unittest.TestCase):
    def test_help(self):
        app = test_app.test_client()

        hello = app.get('/api')

        body = json.loads(str(hello.data, 'utf8'))
        self.assertEqual(body['Hello'], 'World!')


if __name__ == '__main__':
    unittest.main()
