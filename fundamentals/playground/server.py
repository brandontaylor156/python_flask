from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play/<int:times>/<string:color>/')
def index(times, color):
    return render_template("index.html", color=color, times=times)	# notice the 2 new named arguments!

if __name__=="__main__":
    app.run(debug=True)
