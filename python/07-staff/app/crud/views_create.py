# -*- coding:utf-8 -*-
from app.crud import crud 
from flask import render_template,request, jsonify
from app.forms import EmployeeAddForm
from app.orm import ORM
from app.models import Employee, Hobby 
from app.crud.views_common import dt

@crud.route('/',methods=("GET","POST"))
@crud.route("/create/",methods=("GET","POST"))
def create():
    data = dict(
            title="录入员工"
            )
    if request.method=="POST":
        res = dict(code=0)
        form = EmployeeAddForm()
        print('form:',form)
        if form.validate():
            emp_id=save_employee(form)
            session= ORM.db()
            try:
                for v in form.hobby.data:
                    hobby = Hobby(
                            employee_id=emp_id,
                            hobby_key=int(v),
                            createdAt=dt(),
                            updatedAt=dt()
                            )
                    session.add(hobby)
            except Exception as e:
                session.rollback()
            else:
                session.commit()
            finally:
                session.close()
            res["code"] = 1
        else:
            print('errors:', form.errors)
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        return render_template("create.html", data=data)

# 保存员工数据
def save_employee(form):
    session = ORM.db()
    try:
        employee= Employee(
                name=form.name.data,
                job=int(form.job.data),
                sex=int(form.sex.data),
                edu=int(form.edu.data),
                birth=form.birth.data,
                email=form.email.data,
                phone=form.phone.data,
                info=form.info.data,
                face=form.face.data,
                createdAt=dt(),
                updatedAt=dt()
                )
        session.add(employee)
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return employee.id
