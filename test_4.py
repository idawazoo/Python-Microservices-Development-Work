import unittest
import os


class TestMyApp(unittest.TestCase):
    def setUp(self):
        http_server = os.environ.get('HTTP_SERVER')

        if http_server is not None:
            from webtest import TestApp
            self.app = TestApp(http_server)
        else:
            from error_handle_2 import app as test_app
            from flask_webtest import TestApp
            self.app = TestApp(test_app)

    def test_help(self):
        hello = self.app.get('/api')

        self.assetEqual(hello.json['Hello'], 'World!')


if __name__ == '__main__':
    unittest.main()
