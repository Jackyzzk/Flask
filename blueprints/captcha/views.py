from . import bp
from flask import request, abort, make_response
from .gen import captcha
from redis import StrictRedis


sr = StrictRedis('127.0.0.1')


@bp.route('/image')
def generate_image():
    img_id = request.args.get('img_id', None)
    if not img_id:
        return abort(403)
    name, text, image = captcha.generate_captcha()
    sr.set('Img_Id' + img_id, text, 3600)

    res = make_response(image)
    return res



