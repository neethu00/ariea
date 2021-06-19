from typing import Text
from flask import Blueprint, render_template , request ,flash,redirect,url_for
from flask.helpers import flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from  . import db

from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])

def login():    
    #data = request.form
    #print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:

            if check_password_hash(user.password, password):
                return render_template('home.html')
                login_user(user,remember=True)

                flash("Logged in Successully", category ="success")
            else:
                flash('incorrect password', category='error')
        else:
                flash('user not exist')



    return render_template('login.html', text="Testing",user="ananda", boolean=True) #passingvariable to html

@auth.route('/logout')

@login_required

def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])

def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname= request.form.get('firstname')
        password=request.form.get('password')
        password1=request.form.get('password1')
        
        user = User.query.filter_by(email=email).first()
       
        if user:
            
            flash('user exists')
        elif len(email) < 4:
            flash('email greater than 4', category='error')
        elif len(firstname) < 2:
             flash('firstname less than 4', category='error')

        elif password != password1:
            flash('email greater than 4')

        elif len(password) < 7:
            pass

        else:
            new_user = User(email=email,firstname=firstname,password=generate_password_hash(password,method='sha256'))

            
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)

            flash('account created',category='success')
            return redirect(url_for('views.home'))

            #addd user to the database

            



    return render_template('sign_up.html')        
