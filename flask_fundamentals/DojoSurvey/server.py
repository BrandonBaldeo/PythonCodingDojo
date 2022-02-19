from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form',methods=['POST'])
def handle_form():
    session['first_name']=request.form['first_name']
    session['dojo_location']=request.form['dojo_location']
    session['fav_language']=request.form['fav_language']
    session['comments']=request.form['comments']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')



if __name__=="__main__":
    app.run(debug=True) 