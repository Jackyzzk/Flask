from flask import Blueprint


bp = Blueprint('bp_captcha', __name__)

from .views import *

