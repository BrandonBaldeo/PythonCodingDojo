from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html',row=8,col=8,color1='red',color2='black')

@app.route('/<int:col>')
def col(col):
    return render_template('index.html',row=8,col=col,color1='red',color2='black')

@app.route('/<int:col>/<int:row>')
def colrow(col,row):
    return render_template('index.html',row=row,col=col,color1='red',color2='black')

@app.route('/<int:col>/<int:row>/<string:color1>/<string:color2>')
def colors(col,row,color1,color2):
    return render_template('index.html',row=row,col=col,color1=color1,color2=color2)

if __name__=='__main__':
    app.run(debug=True)