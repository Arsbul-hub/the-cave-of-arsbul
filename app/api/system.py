# -*- coding: utf-8 -*-

from flask import jsonify, request, url_for
from app import db
from app.models import SystemEvent
from app.api.auth import token_auth
from app.api import bp
from app.api.errors import bad_request
#from app.api.auth import token_auth
from datetime import datetime

@bp.route('/system', methods=['POST'])
@token_auth.login_required
def get_systemdatetime():
    data = { 'time': int(datetime.utcnow().timestamp()) }
    return jsonify(data)
    
@bp.route('/system/address', methods=['GET'])
def get_addresses():
    data = { 'addresses': [
                {'address': 'г.Электросталь, ул. Сталеваров 19',
                 'type':'Корпус №1',
                 'timestart': 8,
                 'timeend': 19
                },
                {'address': 'г.Электросталь, ул. Первомайская 19',
                 'type':'Корпус №2',
                 'timestart': 8,
                 'timeend': 19
                },
                {'address': 'г.Электросталь, ул. Первомайская 19Б',
                 'type':'Корпус технической школы',
                 'timestart': 8,
                 'timeend': 19
                },
                {'address': 'г.Электросталь, ул. Первомайская 17',
                 'type':'Общежитие',
                 'timestart': 6,
                 'timeend': 22
                },
                {'address': 'г.Электросталь, ул. Спортивная 12',
                 'type':'Корпус №3',
                 'timestart': 8,
                 'timeend': 19
                } 
            ] 
        }
    
    return jsonify(data)