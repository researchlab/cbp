# -*- coding: utf-8 -*-
import os 
DEBUG = True
SECRET_KEY = os.urandom(24) # 生成SECRET_KEY 
CSRF_ENABLED = True  # 开启CSRF 保护
