from flask import jsonify, request
from app import db
from app.models import TestUser
from app.api import bp
from app.api.errors import bad_request


@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data or 'card' not in data:
        return bad_request('must include username, email, card and password fields')
    if TestUser.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if TestUser.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email')
    if TestUser.query.filter_by(card=data['card']).first():
        return bad_request('please use a different card')
    user = TestUser()
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    return response


@bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return bad_request('must include username and password fields')
    user = TestUser.query.filter_by(username=data['username'],password=data['password']).first()
    if user:
        if user.check_token():
            data = { 'token': user.get_token() }
            return jsonify(data)
        else:
            return bad_request('user is active')
    else:
        return bad_request('use different username or password')


@bp.route('/signout/<username>', methods=['GET'])
def signout(username):
    if username:
        user = TestUser.query.filter_by(username=username).first()
        if user:
            user.revoke_token()
            response = jsonify(user.to_dict())
            response.status_code = 200
            return response
        else:
            return bad_request('use different username')
    else:
        return bad_request('must include username fields')