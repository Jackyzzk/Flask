from flask import Blueprint

# 蓝图 实际上就是把一部分功能打包成 python 的包
# 对于b站来说，有很多分类，每一个分类又有若干个子功能，每一个功能可能有多个url
# 在 __init__ 初始化蓝图，在 views 注册路由

# 1.初始化蓝图
bp = Blueprint('bp', __name__)

# 从 views 导入一定要写在最后，不然会出现循环导入
from .views import *
# 执行完这一句话以后，__init__ 就有了 ping 模块
