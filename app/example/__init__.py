from flask import Blueprint

bp = Blueprint('example', __name__)

from . import routes
