""" from flask import Flask
app = Flask(__name__)
app.config.from_object('prod_settings.Config')
print(app.config) """

from konfig import Config
from flask import Flask
c = Config('settings.ini')
app = Flask(__name__)
app.config.update(c.get_map('flask'))
print(app.config['SQLURI'])