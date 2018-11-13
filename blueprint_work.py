from flask import Flask, jsonify, request
from api.teams import teams

app = Flask(__name__)
app.register_blueprint(teams)


@app.route('/api')
def my_microservice():
    response = jsonify({'hello': 'World!'})
    return response


if __name__ == '__main__':
    print(app.url_map)
    app.run()
