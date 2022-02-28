from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    for user in users:
        print(user.first_name)
    return render_template('read.html', users = users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
    }
    new_user_id = User.create_user(data)
    return redirect("/")

@app.route('/<int:user_id>')
def one_User(user_id):
    data = {
        'user_id': user_id
    }
    user = User.one_user(data)
    print(user)
    return render_template('show.html', user = user)

@app.route("/<int:user_id>/edit")

def edit_User(user_id):
    data = {
        'user_id': user_id
    }
    user = User.one_user(data)
    print(user)
    return render_template("edit.html", user=user)

@app.route("/edit_user/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    data = {
        "user_id" : user_id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
    }
    User.edit_user(data)
    return redirect("/")

@app.route("/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        'user_id': user_id
    }
    user = User.delete_user(data)
    print(user)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)