# -*- coding: utf-8 -*-
from app.crud import crud 
from flask import request, redirect, url_for 
from app.models import Employee, Hobby 
from app.orm import ORM 

@crud.route("/delete/", methods=("GET",))
def delete():
    id = request.args.get("id", None)
    if id:
        session = ORM.db() 
        try:
            employee=session.query(Employee).filter_by(id=int(id)).first()
            hob = session.query(Hobby).filter_by(employee_id=int(id)).all()
            session.delete(employee)
            for item in hob:
                session.delete(item)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
    return redirect(url_for("crud.read_list"))
