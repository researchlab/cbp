# -*- coding: utf-8 -*-
import os 
from flask import Blueprint 

root = os.path.dirname(
        os.path.dirname(__file__)
)

crud = Blueprint(
        "crud",
        __name__,
        static_folder=os.path.join(root,"static"),
        template_folder=os.path.join(root, "templates")
        )

import app.crud.views_common 
import app.crud.views_create 
import app.crud.views_delete 
import app.crud.views_read_list 
import app.crud.views_read_one 
import app.crud.views_update
