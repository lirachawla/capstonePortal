import random
import string
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt as sha
from flask_session import Session
from flask_mail import Mail, Message
from app import *
auth = Blueprint('auth', __name__)

@auth.route('/ee35d8da/', methods=['POST','GET'])
def route1():
    return redirect(url_for('grp_auth.register'))

@auth.route('/d07871c/',methods=['POST','GET'])
def route2():
    return redirect(url_for('grp_auth.register'))

@auth.route('/d598ca/', methods=['POST','GET'])
def login():
    try:
        session.clear()
        if request.method== 'GET':
            return render_template('login.html',SITE_KEY=SITE_KEY)
        else:
            email=request.form['email']
            password=request.form['password']
            phash = query_db("select password from Mentors where email = %s", (email, ))
            mentorid = query_db("select mentor_id from Mentors where email = %s", (email, ))
            # captcha_response = request.form['g-recaptcha-response']

            # if is_human(captcha_response):
            if True:
                if phash is None:
                    flash("User does not exist","danger")
                    return render_template("login.html",SITE_KEY=SITE_KEY)

                if sha.verify(password, phash[0][0]):
                    session["user_id"] = email
                    session["mentor_id"] = mentorid[0][0]
                    if query_db("select mentor_id from Heads where mentor_id=%s", (mentorid[0][0], )):
                        session["admin"] = True
                    else:
                        session["admin"] = False
                    flash("Login Successful", "success")
                    return redirect(url_for('mentor.mygroups'))
                else:
                    flash("Incorrect Password","danger")
                    return redirect(url_for('auth.login'))
            else:
                flash("Sorry. Bots not allowed!","danger")
                return redirect(url_for('auth.login'))
    except Exception as e:
        flash("Something went wrong!", 'danger')
        return redirect(url_for('auth.login'))

@auth.route('/logout/')
def logout():
    try:
        session.clear()
        return redirect(url_for("auth.login"))
    except Exception as e:
        flash("Something went wrong!", 'danger')
        return redirect(url_for("auth.login"))

@auth.route('/a77d1b4b/',methods=['POST','GET'])
def signup():
    try:
        cur = mysql.connection.cursor()
        if request.method== 'GET':
            return render_template('signup.html',SITE_KEY=SITE_KEY)
        else:
            name=request.form['name']
            email=request.form['email']
            password=request.form['password']
            confpassword=request.form['confpassword']
            # captcha_response = request.form['g-recaptcha-response']

            # if is_human(captcha_response):
            if True:
                if password!=confpassword:
                    flash("Passwords don't match","danger")
                    return render_template("signup.html",SITE_KEY=SITE_KEY)

                if query_db("select email from Mentors where email = %s", (email,)) is not None:
                    flash("User already taken","danger")
                    return render_template("signup.html",SITE_KEY=SITE_KEY)

                password=sha.encrypt(password)
                cur.execute('insert into Mentors(name,email,password) values(%s,%s,%s)',(
                    name,
                    email,
                    password,
                    ))
                mysql.connection.commit()
                return redirect(url_for("auth.login"))
            else:
                flash("Sorry. Bots not allowed!","danger")
                return redirect(url_for('auth.login'))
    except Exception as e:
        mysql.connection.rollback()
        flash("Something went wrong!", 'danger')
        return redirect(url_for('auth.signup'))
    finally:
        cur.close()

@auth.route('/d598ca_reset/', methods=['POST','GET'])
def reset_link():
    try:
        cur = mysql.connection.cursor()
        if request.method=="GET":
            return render_template("reset_link.html", SITE_KEY=SITE_KEY)
        else:
            email_id = request.form["email"]
            # captcha_response = request.form['g-recaptcha-response']
            
            # if is_human(captcha_response):
            if True:
                records = query_db("SELECT * FROM Mentors where email=%s", (email_id, ))
                if records is None:
                    flash("Incorrect Email ID", "danger")
                else:
                    link = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
                    cur.execute("UPDATE Mentors set reset_link=%s where email=%s", (link, email_id, ))

                    link = "http://172.31.3.184/reset/"+link

                    ## Composing Mail
                    title="Capstone Project Mentor Password Reset Request"
                    sender="no-reply@thapar.edu"
                    recipients = [email_id]
                    message_html = "Your request has been received. Use this link to reset your password: <br><br> <a href=\""+link+"\">"+link+"</a>"
                    send_mail(title,sender,recipients,message_html) # Sending Mail
                    ## End of Mail
                    mysql.connection.commit()
                    flash("Reset Link Sent", "success")
                return redirect(url_for('auth.reset_link'))
            else:
                flash("Sorry. Bots not allowed!","danger")
                return render_template("reset_link.html",SITE_KEY=SITE_KEY)
    except Exception as e:
        mysql.connection.rollback()
        flash("Something went wrong!", 'danger')
        return redirect(url_for('auth.reset_link'))
    finally:
        cur.close()
        

@app.route('/reset/<string:reset_link>/', methods=["GET", "POST"])
def reset_password(reset_link):
    try:
        cur = mysql.connection.cursor()
        if request.method=="GET":
            records = query_db("SELECT * FROM Mentors where reset_link=%s", (reset_link, ))
            verified = False
            if records is not None:
                verified = True
            return render_template("reset_password.html", **locals(), SITE_KEY=SITE_KEY)
        else:
            records = query_db("SELECT * FROM Mentors where reset_link=%s", (reset_link, ))[0][2]
            password = request.form["password"]
            confpassword = request.form["confpassword"]
            # captcha_response = request.form['g-recaptcha-response']
            # if is_human(captcha_response):
            if True:
                if password!=confpassword:
                    flash("Passwords don't match","danger")
                    return redirect(url_for('auth.login'))
                    # return render_template("reset_password.html",SITE_KEY=SITE_KEY)    
                else:
                    password=sha.encrypt(password)
                    cur.execute('UPDATE Mentors SET password=%s, reset_link=NULL where email=%s',(
                        password,
                        records,
                    ))
                    mysql.connection.commit()
                    flash("Password Reset Successful", "success")
            else:
                flash("Sorry. Bots not allowed!","danger")
            return redirect(url_for('auth.login'))
    except Exception as e:
        mysql.connection.rollback()
        flash("Something went wrong!", 'danger')
        return redirect(url_for('auth.login'))
    finally:
        cur.close()
