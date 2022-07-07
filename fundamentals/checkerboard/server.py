from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def normalBoard():
    return render_template("index.html", rows=8, squares=8, color1='blue', color2='black')

@app.route('/<int:dimensionNum>')
def oneDimInput(dimensionNum):
    return render_template("index.html", rows=dimensionNum, squares=dimensionNum, color1='blue', color2='black')

@app.route('/<int:rowNum>/<int:squareNum>/')
def twoDimInput(rowNum, squareNum):
    return render_template("index.html", rows=rowNum, squares=squareNum, color1='blue', color2='black')

@app.route('/<int:rowNum>/<int:squareNum>/<string:color1>/<string:color2>')
def colorInput(rowNum, squareNum, color1, color2):
    return render_template("index.html", rows=rowNum, squares=squareNum, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)    