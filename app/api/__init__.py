from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens, systemevents, passes, system, testuser
