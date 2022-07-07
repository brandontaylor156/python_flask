from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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

