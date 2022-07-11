from flask import Flask, render_template, request, redirect, session
import random, sys, datetime
app= Flask(__name__)
app.secret_key = 'brando'

@app.route('/')
def index(): 
    if 'game_over' not in session:
        session['game_over'] = False
    
    if session['game_over'] == True:
            session.clear()

    if 'gold_amount' not in session or 'activity_log' not in session or 'moves_left' not in session or 'target' not in session:
        session['gold_amount'] = 0
        session['activity_log'] = ""
        session['moves_left'] = 15
        session['target'] = 200

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if session['moves_left'] == 0 or session['gold_amount'] >= session['target']:
        session['game_over'] = True
        return redirect('/')

    session['moves_left'] -= 1

    if request.form['quest'] == 'farm':
        amount_earned = random.randint(10,20)
    elif request.form['quest'] == 'cave':
        amount_earned = random.randint(5,10)
    elif request.form['quest'] == 'house':
        amount_earned = random.randint(2,5)
    elif request.form['quest'] == 'casino':
        amount_earned = random.randint(-50,50)

    session['gold_amount'] += amount_earned

    if session['gold_amount'] < 0:
        session['gold_amount'] = 0

    if amount_earned >= 0:
        session['activity_log'] = "<div style='color:green'>Earned " + str(amount_earned) + " golds from the " + request.form['quest'] + "! (" + str(datetime.datetime.today())[:-7] + ")</div>" + session['activity_log']
    else:
        session['activity_log'] = "<div style='color:red'>Lost " + str(amount_earned)[1:] + " golds at the " + request.form['quest'] + "... Ouch.. (" + str(datetime.datetime.today())[:-7] + ")</div>" + session['activity_log']
    
    
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)