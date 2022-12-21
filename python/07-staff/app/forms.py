#-*- coding: utf-8 -*-
from flask_wtf import Form 
from wtforms.fields import StringField, IntegerField, SelectField, DateField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp
from app.params import *

# 录入员工表单
class EmployeeAddForm(Form):
    name = StringField('姓名', validators=[ DataRequired("姓名不能为空! ")])
    job = SelectField("职位", choices=[(k+1,v) for k,v in enumerate(job_list)], coerce=int, validators=[DataRequired("职位不能为空!")])
    sex = SelectField(
            "性别",
            choices=[(k+1,v) for k,v in enumerate(sex_list)],
            coerce=int,
            validators=[
                DataRequired('性别不能为空! ')
                ]
            )
    edu = SelectField(
            "学历",
            choices=[(k+1, v) for k,v in enumerate(edu_list)],
            coerce=int,
            validators=[
                DataRequired("学历不能为空!")
                ]
            )
    birth=DateField(
            "生日",
            validators=[
                DataRequired("生日不能为空!")
                ]
            )
    email = StringField(
            "邮件",
            validators=[
                DataRequired("邮箱不能为空!"),
                Email("邮箱格式不正确!")
                ]
            )
    phone = StringField(
            "手机",
            validators=[
                DataRequired("手机不能为空!"),
                Regexp("1[345789]\\d{9}",message="手机格式不正确!")
                ]
            )
    hobby = SelectMultipleField(
            "爱好",
            choices=[(k+1,v) for k,v in enumerate(hobby_list)],
            coerce=int,
            validators=[
                DataRequired("爱好不能为空!")
                ]
            )
    info = TextAreaField(
            u"介绍",
            validators=[
                DataRequired(u"介绍不能为空!")
                ]
            )
    face=StringField(
            "头像",
            validators=[
                DataRequired("头像不能为空!")
                ]
            )

# 修改员工表单
class EmployeeEditForm(Form):
    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空！")
        ]
    )
    name = StringField(
        "姓名",
        validators=[
            DataRequired("姓名不能为空！")
        ]
    )
    job = SelectField(
        "职位",
        choices=[(k + 1, v) for k, v in enumerate(job_list)],
        coerce=int,
        validators=[
            DataRequired("职位不能为空！")
        ]
    )
    sex = SelectField(
        "性别",
        choices=[(k + 1, v) for k, v in enumerate(sex_list)],
        coerce=int,
        validators=[
            DataRequired("性别不能为空！")
        ]
    )
    edu = SelectField(
        "学历",
        choices=[(k + 1, v) for k, v in enumerate(edu_list)],
        coerce=int,
        validators=[
            DataRequired("学历不能为空！")
        ]
    )
    birth = DateField(
        "生日",
        validators=[
            DataRequired("生日不能为空！")
        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ]
    )
    phone = StringField(
        "手机",
        validators=[
            DataRequired("手机不能为空！"),
            Regexp("1[345789]\\d{9}", message="手机格式不正确！")
        ]
    )
    hobby = SelectMultipleField(
        "爱好",
        choices=[(k + 1, v) for k, v in enumerate(hobby_list)],
        coerce=int,
        validators=[
            DataRequired("爱好不能为空！")
        ]
    )
    info = TextAreaField(
        u"介绍",
        validators=[
            DataRequired(u"介绍不能为空！")
        ]
    )
    face = StringField(
        "头像",
        validators=[
            DataRequired("头像不能为空！")
        ]
    )
