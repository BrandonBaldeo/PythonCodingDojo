from flask_app.models.dojos import Dojo
from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', dojos = dojos)


@app.route('/dojos/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        'name' : request.form['name']
    }
    add_dojo = Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_info(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    show_one_dojo = Dojo.show_one_dojo(data)
    print(show_one_dojo)
    return render_template('show_info.html', dojo = show_one_dojo)

@app.route('/add_ninja')
def add_ninja():
    Dojos = Dojo.get_all()
    return render_template('add_ninja.html', Dojos = Dojos)

@app.route('/new_ninja', methods=['POST'])
def new_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    add_ninja = Dojo.add_ninja(data)
    return redirect('/dojos')