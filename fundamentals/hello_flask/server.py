from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def sayName(name):
    return f"Hey {name.title()}!"

@app.route('/repeat/<int:number>/<string:word>')
def sayWord(number, word):
    return word*number

@app.route('/<anything>')
def errorMessage(anything):
    if anything != 'dojo' and not anything.startswith('say/<string:name>') and not anything.startswith('repeat/<int:number>/<string:word>'):
        return "Sorry! No response"


if __name__=="__main__":
    app.run(debug=True)

