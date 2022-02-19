from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=1
    else:
        session['counter']=session['counter']+1
    return render_template('index.html')

@app.route('/',methods=['POST'])
def counter():
    session['counter']+=1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True) 