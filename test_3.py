import unittest
from flask_webtest import TestApp
from error_handle_2 import app as test_app

#requires server to be up
class TestMyApp(unittest.TestCase):
    def test_help(self):
        app = TestApp(test_app)

        hello = app.get('/api')

        self.assetEqual(hello.json['Hello'], 'World!')

if __name__ == '__main__':
    unittest.main()