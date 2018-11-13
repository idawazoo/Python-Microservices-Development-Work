import unittest
import json
from error_handle_2 import app as test_app

_404 = ('philtest 404 error.')


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()

    def test_raise(self):
        hello = self.app.get('/api')
        print("-> {0}".format(hello.data))
        body = json.loads(str(hello.data, 'utf8'))
        print("--> {0}".format(body))
        self.assertEqual(body['code'], 500)

    def test_proper_404(self):
        hello = self.app.get('/ajdlka')

        self.assertEqual(hello.status_code, 404)

        print("*> {0}".format(hello.data))

        body = json.loads(str(hello.data, 'utf-8'))

        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], '404: not Found')
        self.assertEqual(body['description'], _404)


if __name__ == '__main__':
    unittest.main()
