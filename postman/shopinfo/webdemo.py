# coding=utf-8
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request
import time, json
import os
from flask import request

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF', 'xmind'])

@app.route("/test", methods=['GET','POST','PUT','DELETE'],strict_slashes=False)
def api_test():
    if request.method == 'GET':
        return jsonify({"msg":"getsuccess"})
    elif request.method == 'POST':
        return jsonify({"msg":"postsuccess"})
    elif request.method == 'PUT':
        return jsonify({"msg": "putsuccess"})
    elif request.method == 'DELETE':
        return jsonify({"msg":"deletesuccess"})


@app.route('/api/login', methods=['POST'], strict_slashes=False)
def api_login():
    data = request.get_json()
    print('<Request> url= {url}, body= {body}'.format(url=request.url, body=json.dumps(data, ensure_ascii=False)))
    if data["username"] == "daxiong" and data["password"] == '123456':
        return jsonify({
            "httpstatus": 200,
            "add": {
                "city": "shanghai",
                "address": "pudong"
            },
            "info": {
                "name": "shenji",
                "age": 28
            },
            "msg": "success",
            "token": "GWEBH23E2H324H2G34324GH3242342"
        })
    else:
        return jsonify({"code": '001', "msg": "用户名或密码错误", })


@app.route('/api/getproductinfo', methods=['GET'], strict_slashes=False)
def api_getProductInfo():
    data = request.args.get('productid')
    if data == '8888':
        return jsonify({"httpstatus": 200,
                        "data": [
                            {
                                "productid": int(data),
                                "productname": "陕西红富士5斤装",
                                "SKU": "YRHJSJ990",
                                "price": 49.9,
                                "productdesc": "果形优美,大小均匀,果面洁净,色泽鲜艳。吃起来口感香甜可口,硬度适中,肉质脆密,含糖量高。"

                            }
                        ]})

    elif data == '2222':
        return jsonify({"httpstatus": 200,
                        "data": [
                            {
                                "productid": data,
                                "productname": "智利蓝莓10盒装",
                                "SKU": "RIEUR33829",
                                "price": 119.9,
                                "productdesc": "蓝莓果实中含有丰富的营养成分,具有防止脑神经老化、强心、抗癌、软化血管、增强人机体免疫等功能。"

                            }
                        ]})
    else:
        return jsonify({"code": '1001', "msg": "您请求的商品不存在！", })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
