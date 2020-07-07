from . import bp
from flask import request, jsonify


@bp.route('/ajax1', methods=['POST'])
def ajax1():
    res = {}
    name = request.json.get('name')
    res['name'] = 'ok' if name else '用户名不能为空'
    return jsonify(res)


@bp.route('/ajax2', methods=['POST'])
def ajax2():
    res = {}
    pwd = request.json.get('pwd')
    res['pwd'] = 'ok' if pwd else '密码不能为空'
    return jsonify(res)


@bp.route('/ajax3', methods=['POST'])
def ajax3():
    res = {}
    # data = request.get_json()  # data 是一个字典
    page = request.json.get('page')
    res['page'] = page if page else '转向不能为空'
    return jsonify(res)

# 字典与 Json 的相互转化
# 在 python 中，字典 -> Json : jsonify(字典)
# 在 javascript 中，字典 -> Json : JSON.stringify(字典)



