# -*- coding: utf-8 -*-

from flask import jsonify, request, url_for
from app import db
from app.models import Pass
from app.api.auth import token_auth
from app.api import bp
from app.api.errors import bad_request


@bp.route('/passes', methods=['POST'])
@token_auth.login_required
def get_passes():
    data = request.get_json() or {}
    if 'page' not in data:
        page = 1
    else:
        page = int(data['page'])
    if 'per_page' not in data:
        per_page = 10
    else:
        per_page = min(int(data['per_page']), 100)
    data = Pass.to_collection_dict(Pass.query,
                                   page,
                                   per_page,
                                   'api.get_passes')
    return jsonify(data)


@bp.route('/pass_by_id/{id}', methods=['POST'])
@token_auth.login_required
def get_pass_by_id(id):
    p = Pass.query.filter_by(pass_code=id) \
        .first_or_404()  # description='please use a different id. {}'.format(id))
    return jsonify(p.to_dict())


@bp.route('/pass_by_code/{pass_code}', methods=['POST'])
@token_auth.login_required
def get_pass_by_pass_code(pass_code):
    p = Pass.query.filter_by(pass_code=pass_code) \
        .first_or_404()  # description='please use a different pass_code. {}'.format(pass_code))
    return jsonify(p.to_dict())


@bp.route('/pass/create', methods=['POST'])
@token_auth.login_required
def create_pass():
    data = request.get_json() or {}
    if 'pass_code' not in data or 'pass_holder' not in data:
        return bad_request('for create skip must include pass_code and pass_holder')
    if Pass.query.filter_by(pass_code=data[
        'pass_code']).first() is not None:  # description='please use a different pass_code. {}'.format(data['pass_code']))
        return 'please use a different pass_code. ' + data['pass_code']
    p = Pass()
    p.from_dict(data)
    db.session.add(p)
    db.session.flush()
    db.session.refresh(p)
    db.session.commit()
    response = jsonify(p.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.create_pass', pass_code=p.pass_code)
    return response


@bp.route('/pass/delete', methods=['POST'])
@token_auth.login_required
def delete_pass():
    data = request.get_json() or {}
    if 'id' not in data:
        return bad_request('for delete pass must include id')
    p = Pass.query.filter_by(id=data['id']) \
        .first_or_404()  # description = 'please use a different id={}'.format(id))
    db.session.delete(p)
    db.session.commit()
    response = jsonify(p.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.delete_pass', id=p.id)
    return response


@bp.route('/pass/change', methods=['POST'])
@token_auth.login_required
def change_pass():
    data = request.get_json() or {}
    print("!")
    print(data)
    if 'id' not in data:
        return bad_request('please include id or page, per_page')

    p = Pass.query.filter_by(id=data['id']).first_or_404()  # description='please use a different id. {}'.format(id))
    p.from_dict(data)
    db.session.flush()
    db.session.refresh(p)
    db.session.commit()
    response = jsonify(p.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.change_pass', pass_code=p.pass_code)
    return response
