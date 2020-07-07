from flask import Blueprint

bp = Blueprint('bp_ajax', __name__)

from .views import *
