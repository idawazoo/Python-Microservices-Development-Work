from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime


def render_email(**data):
    with open('email_template.eml') as f:
        template = Template(f.read())
    return template.render(**data)


data = {
    'date': format_datetime(datetime.now()),
    'to': 'bob@example.com',
    'from': 'tarek@ziade.org',
    'subject': "Your Terak's Burger order",
    'name': 'Bob',
    'items': [
        {
            'name': 'Cheeseburger',
            'price': 4.5
        },
        {
            'name': 'Fries',
            'price': 2.0
        }
    ]
}

print(render_email(**data))
