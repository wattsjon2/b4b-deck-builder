from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from b4b.forms import UserLoginForm
from b4b.models import db, User

#imports for flask login
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth',__name__,template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserLoginForm()
    counter = 0
    try:
        if request.method == 'POST' and form.validate_on_submit():
            
            email = form.email.data
            password = form.password.data
            print(email, password)

            allUsers = User.query.filter_by(email = form.email.data)
            
            for user in allUsers:
                counter += 1
                flash(f'There is already an account for this email {email}.', "user-exists")
                return render_template('signup.html', form = form, counter = counter)
            
            if counter == 0:
                user = User(email,password = password)
                db.session.add(user)
                db.session.commit()

                flash(f'You have successfully created a user account for {email}.', "user-created")

                return redirect(url_for('auth.signin'))
                
    except:
        raise Exception('Invalid Form Data: Please check your form...')

    return render_template('signup.html', form = form, counter = counter)


@auth.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserLoginForm()
    passwordfail = False

    try: 
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            #Query user table fpr user with info
            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You werer sucessfully loged in', 'auth-success')
                session['show_decks'] = 'False'

                return redirect(url_for('site.home'))
            else:
                passwordfail = True
                flash('Your Email/Password is incorrect', 'auth-failed')
                return render_template('signin.html', form = form, passwordfail = passwordfail)
    except:
        raise Exception('Invalid form data: Please check your form')
    
    return render_template('signin.html', form = form, passwordfail = passwordfail)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))