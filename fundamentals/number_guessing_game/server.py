from flask import Flask, render_template, request, redirect, session
import random, sys
app= Flask(__name__)
app.secret_key = 'brando'

@app.route('/')
def count():
    if 'random_num' not in session or 'times_guessed' not in session:
        session['random_num'] = random.randint(1,100)
        session['times_guessed'] = 0
        print(session['times_guessed'])
    
    return render_template("index.html")

@app.route('/make_guess', methods=['POST'])
def make_guess():
    session['times_guessed'] += 1
    if int(request.form['user_guess'])==session['random_num']:
        return redirect('/success')
    elif int(request.form['user_guess']) < session['random_num']:
        return redirect('/too_low')
    else:
        return redirect('/too_high')

@app.route('/success')
def success():
    guesses = session['times_guessed']
    session['random_num'] = random.randint(1,100)
    session['times_guessed'] = 0
    return render_template("index.html", result="Success!", color='success', guesses=guesses)

@app.route('/too_low')
def too_low():
    return render_template("index.html", result="Too low!", color='danger')

@app.route('/too_high')
def too_high():
    return render_template("index.html", result="Too high!", color='danger')

if __name__=="__main__":
    app.run(debug=True)