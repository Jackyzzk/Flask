# 在 __init__ 初始化蓝图，在 views 注册路由
# 从"."里面导入已经初始化好的蓝图，会优先查看 __init__.py 里面有没有这个模块
from . import bp


# 2.使用蓝图注册路由
@bp.route('/ping')
def ping():
    return 'pong'
