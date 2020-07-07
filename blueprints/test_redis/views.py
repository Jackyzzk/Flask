from . import bp
from redis import StrictRedis


@bp.route('/redis')
def redis():
    sr = StrictRedis(host='127.0.0.1')

    try:
        ret = sr.set('name', 'jackyzzk')
        res = sr.get('name')
        print(ret)
        return res
    except Exception as e:
        print(e)