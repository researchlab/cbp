# -*- coding: utf-8 -*-
from app.crud import crud 
from flask import render_template, request, redirect, url_for 
from app.models import Employee, Hobby 
from app.orm import ORM 

@crud.route("/read/one/", methods=("GET", "POST"))
def read_one():
    id = request.args.get("id", None)
    if id:
        data = dict(
                title="员工详情"
                )
        session = ORM.db()
        try:
            data["emp"] = session.query(Employee).filter_by(id=int(id)).first()
            data['hob'] = session.query(Hobby).filter_by(employee_id=int(id)).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return render_template("read_one.html", data=data)
    else:
        return redirect(url_for("crud.read_list"))
