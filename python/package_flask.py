# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wAIxi'
__date__ = '2021/4/21'
__description__ = doc description
"""
import json
from flask import Flask, request, Response, jsonify, make_response, Blueprint
from flask_cors import *
from typing import List

"""创建实例"""

app = Flask(
    __name__,
    template_folder='./',
    static_folder='./',
    static_url_path=''
)
CORS(app, supports_credentials=True)  # 设置跨域
api = Blueprint('api', __name__)
app.register_blueprint(api)


@app.route('/predict', methods=['POST'])
def predict():
    post_arg = json.loads(request.data.decode("utf8"))
    source_str_list: List[str] = post_arg['input']
    # todo 对输入进行处理 这里直接将输入作为输出
    res_str_list: List[str] = source_str_list
    final_result = {'code': 0, 'data': res_str_list}
    final_result = make_response(final_result)
    final_result.headers['Access-Control-Allow-Origin'] = '*'
    final_result.headers['Access-Control-Allow-Method'] = '*'
    final_result.headers['Access-Control-Allow-Headers'] = '*'
    return final_result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
