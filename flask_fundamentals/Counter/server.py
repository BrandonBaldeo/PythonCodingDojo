from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destroy_session',methods=['POST'])
def destroy():
    return redirect('index.html')



if __name__=="__main__":
    app.run(debug=True) 