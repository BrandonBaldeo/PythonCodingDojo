from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def home():
    return render_template('index.html',x=3,color='aqua')

@app.route('/play/<int:x>')
def mult(x):
    return render_template('index.html',x=x,color='aqua')

@app.route('/play/<int:x>/<string:color>')
def color(x,color):
    return render_template('index.html',x=x,color=color)

if __name__=='__main__':
    app.run(debug=True)