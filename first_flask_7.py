from flask import Flask, jsonify, request, g
from werkzeug.routing import BaseConverter, ValidationError
import yaml

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}


class RegisterUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]

        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
app.url_map.converters['registered'] = RegisterUser

'''
@app.route('/api', methods=['POST', 'DELETE', 'GET'])
def my_microservice():
    print(request)
    print(request.environ)
    response = jsonify({'hello':'World!'})
    print(response)
    print(response.data)
    return response
'''


@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'


@app.route('/api')
def my_microservice():
    return jsonify({'Hello': g.user})


'''
@app.route('/api/person/<int:person_id>')
def person(person_id):
    response = jsonify({'Hello':person_id})
    return response
'''


@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello hey': name})
    return response


@app.route('/')
def auth():
    print('The raw Authorization header')
    print(request.environ["HTTP_AUTHORIZATION"])
    print("Flask's authorization header")
    print(request.authorization)
    return ""


def yamlify(data, status=200, headers=None):
    _headers = {'Content-Type': 'application/x-yaml'}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers


@app.route('/api2')
def my_microservice2():
    return yamlify(['Hello', 'YAML', 'World!'])


if __name__ == '__main__':
    print(app.url_map)
    app.run()
