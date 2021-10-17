from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt as sha
from flask_session import Session
from validate_email import validate_email
from app import *


grp_auth = Blueprint('grp_auth', __name__)

@grp_auth.route("/register/", methods=['POST', 'GET'])
def register():
    try:
        cur = mysql.connection.cursor()
        if request.method == 'GET':
            return render_template("register.html",SITE_KEY=SITE_KEY)
        else:
            captcha_response = request.form['g-recaptcha-response']
            mentor_email = request.form['mentor_id']
            mentor_id = query_db("select mentor_id from Mentors where email = %s",(mentor_email,))
            if is_human(captcha_response):
            # if True:
                if mentor_id is None:
                    flash("Wrong Mentor Email", 'danger')
                    return redirect(url_for('grp_auth.register'))
                else:
                    if not validate_email(request.form['email']):
                        flash("Enter valid email address", 'danger')
                        return redirect(url_for('grp_auth.register'))
                    leader_id = query_db("select roll_no from Students where roll_no=%s ",(request.form['leader_id'],))
                    student2 = query_db("select roll_no from Students where roll_no=%s ",(request.form['student2'],))
                    student3 = query_db("select roll_no from Students where roll_no=%s ",(request.form['student3'],))
                    student4 = query_db("select roll_no from Students where roll_no=%s ",(request.form['student4'],))
                    if request.form['leader_id'] == request.form['student2'] or request.form['leader_id'] == request.form['student3'] or request.form['leader_id'] == request.form['student4'] or request.form['student2'] == request.form['student3'] or request.form['student2'] == request.form['student4'] or request.form['student4'] == request.form['student3']:
                        flash("Some students have same roll number in the group", 'danger')
                        return redirect(url_for('grp_auth.register'))

                    request_leader = query_db("select leader_roll_no from Requests where leader_roll_no=%s ",(request.form['leader_id'],))
                    request_student2 = query_db("select student2_roll_no from Requests where student2_roll_no=%s ",(request.form['student2'],))
                    request_student3 = query_db("select student3_roll_no from Requests where student3_roll_no=%s ",(request.form['student3'],))
                    request_student4 = query_db("select student4_roll_no from Requests where student4_roll_no=%s ",(request.form['student4'],))
                    if leader_id is not None or student2 is not None or student3 is not None or student4 is not None:
                        flash("Some students are already registered", 'danger')
                        return redirect(url_for('grp_auth.register'))
                    elif request_leader is not None or request_student2 is not None or request_student3 is not None or request_student4 is not None:
                        flash("Some students are already registered", 'danger')
                        return redirect(url_for('grp_auth.register'))
                    elif len(str(request.form.get('phone'))) != 10:
                        flash("Enter a valid 10 digit Phone Number!", 'danger')
                        return redirect(url_for('grp_auth.register'))
                    elif len(str(request.form.get('leader_id'))) != 9 or len(str(request.form.get('student2'))) != 9 or len(str(request.form.get('student3'))) != 9 or (len(str(request.form.get('student4'))) != 9 and len(str(request.form.get('student4'))) != 0):
                        flash("Enter correct Roll Numbers!", 'danger')
                        return redirect(url_for('grp_auth.register'))
                    if request.form['student4']=='':
                        student4 = None
                    else:
                        student4 = request.form['student4']

                    title=request.form.get('title', False)
                    description = request.form.get('description', False)
                    title_des = title+"*93-k+5=H]s]V%"+description
                    cur.execute("INSERT INTO Requests(leader_roll_no, title, student2_roll_no, student3_roll_no, student4_roll_no, email, leader_name, student2_name, student3_name, student4_name, phone, mentor_id) Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                        request.form['leader_id'],
                        title_des,
                        request.form['student2'],
                        request.form['student3'],
                        student4,
                        request.form['email'],
                        request.form['leader_name'],
                        request.form['student2_name'],
                        request.form['student3_name'],
                        request.form['student4_name'],
                        request.form['phone'],
                        mentor_id,
                    ))
                    mysql.connection.commit()
                    flash("Applied Successfully", 'success')
                    return redirect(url_for('grp_auth.register'))
            else:
                flash("Sorry. Bots not allowed!","danger")
                return redirect(url_for('grp_auth.register'))
    except Exception as e:
        mysql.connection.rollback()
        flash("Something went wrong!", 'danger')
        return redirect(url_for('grp_auth.register'))
    finally:
        cur.close()

@grp_auth.route("/objective_register/", methods=['POST', 'GET'])
def objective():
    try:
        cur = mysql.connection.cursor()
        if request.method == 'GET':
            return render_template("objective.html",SITE_KEY=SITE_KEY)
        else:
            captcha_response = request.form['g-recaptcha-response']
            mentor_email = request.form['mentor_id']
            mentor_id = query_db("select mentor_id from Mentors where email = %s",(mentor_email,))
            # if is_human(captcha_response):
            if True:
                if mentor_id is None:
                    flash("Wrong Mentor Email", 'danger')
                    return redirect(url_for('grp_auth.objective'))
                else:
                    if not validate_email(request.form['email']):
                        flash("Enter valid email address", 'danger')
                        return redirect(url_for('grp_auth.objective'))
                    query = query_db("select group_id from Teams where leader_roll_no=%s AND phone=%s AND email=%s",(request.form['leader_id'], request.form['phone'], request.form['email'], ))
                    if query is None:
                        flash("Wrong Credentials", 'danger')
                        return redirect(url_for('grp_auth.objective'))
                    else:
                        group_id = query[0][0]
                        query = query_db("select * from Group_Mentors where group_id=%s AND mentor1_id=%s",(group_id, mentor_id, ))
                        if query is None:
                            flash("Wrong Mentor Email", 'danger')
                            return redirect(url_for('grp_auth.objective'))
                        else:
                            objective = request.form.get('objective_1', "")+"_"+request.form.get('objective_2', "")+"_"+request.form.get('objective_3', "")+"_"+request.form.get('objective_4', "")+"_"+request.form.get('objective_5', "")
                            execute_db("UPDATE Teams SET objective=%s WHERE leader_roll_no=%s;",(
                                objective,
                                request.form['leader_id'],
                            ))
                    flash("Objective Added Successfully", 'success')
                    return redirect(url_for('grp_auth.objective'))
            else:
                flash("Sorry. Bots not allowed!","danger")
                return redirect(url_for('grp_auth.objective'))
    except Exception as e:
        mysql.connection.rollback()
        flash("Something went wrong!", 'danger')
        return redirect(url_for('grp_auth.objective_register'))
    finally:
        cur.close()