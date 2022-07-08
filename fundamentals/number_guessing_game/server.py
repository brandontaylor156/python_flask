frm flask import Flask, render_template, request, redirect, session
import random, sys
app= Flask(__name__)
app.secret_key = 'brando'

@app.route('/')
def count():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/make_guess', methods=['POST'])
def make_guess():
    if int(request.form['user_guess'])==session['random_num']:
        session.pop('random_num')
        return redirect('/success')
    elif int(request.form['user_guess']) < session['random_num']:
        return redirect('/too_low')
    else:
        return redirect('/too_high')

@app.route('/success')
def success():
    session['random_num'] = random.randint(1,100)
    return render_template("index.html", result="Success!", color='success')

@app.route('/too_low')
def too_low():
    return render_template("index.html", result="Too low!", color='danger')

@app.route('/too_high')
def too_high():
    return render_template("index.html", result="Too high!", color='danger')

if __name__=="__main__":
    app.run(debug=True)