# -*- coding: utf-8 -*-

from flask import jsonify, request, url_for
from app import db
from app.models import SystemEvent
from app.api.auth import token_auth
from app.api import bp
from app.api.errors import bad_request
#from app.api.auth import token_auth


@bp.route('/systemevents/get', methods=['POST'])
@token_auth.login_required
def get_systemevents():
    data = request.get_json() or {}
    if 'if' not in data:
        if 'page' not in data:
            page = 1
        else:
            page = int(data['page'])
        if 'per_page' not in data:
            per_page = 10
        else:
            per_page = min(int(data['per_page']), 100)
        data = SystemEvent.to_collection_dict(SystemEvent.query, 
                                              page, 
                                              per_page,
                                              'api.get_systemevents') 
    else:
        id = int(data['id'])
        data = SystemEvent.query(id = id).first().to_dict()
    return jsonify(data)


@bp.route('/systemevents/put', methods=['POST'])
@token_auth.login_required
def put_systemevents():
    data = request.get_json() or {}
    if 'device_mac' not in data or 'event' not in data:
        return bad_request('please include timestamp, device_mac and event')
    systemevents = SystemEvent()
    systemevents.from_dict(data)
    db.session.add(systemevents)
    db.session.flush()
    db.session.refresh(systemevents)
    db.session.commit()
    response = jsonify(systemevents.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.put_systemevents', id=systemevents.id)
    return response

@bp.route('/systemevents/flash', methods=['POST'])
@token_auth.login_required
def flash_systemevents():
    data = request.get_json() or {}
    if 'items' not in data or 'meta' not in data:
        return bad_request('please include items[] and meta{}')
    for item in range(data['meta']['total_items']):
        systemevents = SystemEvent()
        systemevents.from_dict(data['items'][item])
        db.session.add(systemevents)
        db.session.flush()
    db.session.refresh(systemevents)
    db.session.commit()
    response = jsonify({'total_items': data['meta']['total_items']})
    response.status_code = 201
    response.headers['Location'] = url_for('api.put_systemevents', total_items = data['meta']['total_items'])
    return response
