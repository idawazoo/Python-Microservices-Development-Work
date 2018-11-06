from first_flask_4 import app
from flask import url_for

with app.test_request_context():
    print(url_for('person', name='Tarek'))
