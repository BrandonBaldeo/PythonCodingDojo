from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_user():
    
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : request.form['password'],
        "confirm_pass" : request.form['confirm_pass']
    }
    if not User.user_valid(data):
        return redirect('/')

    print(request.form["password"])
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)
    data["password"] = pw_hash

    add_user = User.create_user(data)
    flash('Your account has been created, Please Login')
    session["user_id"] = add_user
    session['user_email']=add_user
    return redirect('/')


@app.route('/login', methods=['POST'])
def login_user():
    data = {
        "email" : request.form['email'],
        "password" : request.form['password']
    }
    if not User.login_validate(data):
        return redirect('/')
    logged_user = User.get_by_email(data)

    session["user_id"] = logged_user.id
    session["user_email"]=logged_user.email
    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    data = {
        "user_id" : session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('dashboard.html', user = user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")