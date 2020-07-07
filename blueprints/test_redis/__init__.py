from flask import Blueprint

bp = Blueprint('bp_redis', __name__)

from .views import *