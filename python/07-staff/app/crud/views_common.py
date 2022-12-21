# -*- coding: utf-8 -*-
import os 
import math 
import datetime 
import uuid 
from app.crud import crud 
from app.params import * 
from flask import request, jsonify 
from werkzeug.utils import secure_filename


@crud.context_processor
def data_params():
    return dict(
            job_list=job_list,
            edu_list=edu_list,
            sex_list=sex_list,
            hobby_list=hobby_list,
            job_param=enumerate(job_list),
            edu_param=enumerate(edu_list),
            sex_param=enumerate(sex_list),
            hobby_param=enumerate(hobby_list)
            )

upload_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "static/uploads"
        )

allowed_ext = set(["jpg","jpeg","png","gif"])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext

@crud.route("/upload/", methods=("POST",))
def upload():
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = "{}{}{}".format(
                datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                uuid.uuid4().hex,
                os.path.splitext(filename)[-1]
                )
        file.save(os.path.join(upload_path, filename))
        return jsonify(
                dict(
                    code=1,
                    image=filename
                    )
                )

def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def page(model):
    page = request.args.get("page", 1)
    page = int(page)
    total = model.count()
    if total:
        shownum = 10
        pagenum = int(math.ceil(total/shownum))
        if page < 1:
            page = 1
        if page > pagenum:
            page= pagenum 
        offset = (page -1)*shownum 
        data = model.limit(shownum).offset(offset).all()
        prev_p = page -1 
        next_p = page +1
        if prev_p < 1:
            prev_p = 1 
        if next_p > pagenum:
            next_p = pagenum 
        arr = dict(
                pagenum=pagenum,
                total=total,
                prev=prev_p,
                next=next_p,
                data=data,
                page=page
                )
    else:
        arr = dict(
                data =[]
                )
    return arr

