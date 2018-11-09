from flask import Blueprint,jsonify

teams = Blueprint('api', __name__, url_prefix="/teams")

_DEVS = ['Tarek', 'Bob']
_OPS = ['Bill']
_TEAMS = {1:_DEVS, 2: _OPS}

@teams.route('/get')
def get_all():
    return jsonify(_TEAMS)

@teams.route('/get/<int:team_id>')
def get_team(team_id):
    return jsonify(_TEAMS[team_id])
