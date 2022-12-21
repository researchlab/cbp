# -*- coding: utf-8 -*-
from app.crud import crud 
from flask import redirect, url_for, request, render_template, jsonify 
from app.models import Employee, Hobby 
from app.orm import ORM 
from app.forms import EmployeeEditForm
from app.crud.views_common import dt 
from sqlalchemy import and_

@crud.route("/update/", methods=("GET","POST"))
def update():
    id = request.args.get("id", None)

    data = dict(
            title="修改员工"
            )
    if request.method == "POST":
        res = dict(code=0)
        form = EmployeeEditForm()
        if form.validate():
            update_emp(form)
            res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        if id:
            data["emp"], hob = get_emp(id)
            hob = [v.hobby_key for v in hob]
            data["hob"] = hob 
            return render_template("update.html", data=data)
        else:
            return redirect(url_for('crud.read_list'))

def get_emp(id):
    session = ORM.db()
    emp, hob = None, None 
    try:
        emp = session.query(Employee).filter_by(id=int(id)).first()
        hob = session.query(Hobby).filter_by(employee_id=int(id)).all()
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return emp, hob

def update_emp(form):
    session = ORM.db() 
    try:
        # 修改员工信息
        emp = session.query(Employee).filter_by(id=int(form.id.data)).first()
        emp.name = form.name.data 
        emp.job = int(form.job.data)
        emp.sex = int(form.sex.data)
        emp.edu = int(form.edu.data)
        emp.birth = form.birth.data
        emp.email = form.email.data 
        emp.phone = form.phone.data 
        emp.info = form.info.data 
        emp.face = form.face.data 
        emp.updatedAt = dt() 
        # 修改爱好
        hob = session.query(Hobby).filter_by(employee_id=int(form.id.data)).all()
        old_hob_keys = [v.hobby_key for v in hob]
        new_hob_keys = [int(v) for v in form.hobby.data]
        # 新增爱好添加到数据库中
        for v in new_hob_keys:
            if v not in old_hob_keys:
                ch = Hobby(
                        employee_id=emp.id,
                        hobby_key=v,
                        createdAt=dt(),
                        updatedAt=dt()
                        )
                session.add(ch)
        for v in old_hob_keys:
            if v not in new_hob_keys:
                ch = session.query(Hobby).filter(
                        and_(
                            Hobby.employee_id==emp.id,
                            Hobby.hobby_key==v
                            )
                        ).first()
                session.delete(ch)
        session.add(emp)
    except Exception as e:
        session.rollback()
    else:
        sessiion.commit()
    finally:
        session.close()
