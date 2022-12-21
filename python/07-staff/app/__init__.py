# -*- coding: utf-8 -*- 
from flask import Flask 
from flask_wtf import CSRFProtect

# 开启表单令牌，防止跨站伪装登录、请求
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__) # 实例化
    app.config.from_object("app.configs")
    csrf.init_app(app)
    from app.crud import crud 
    app.register_blueprint(crud)
    return app 
