from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'brando'

@app.route('/')
def count():
    if 'times_visited' in session:
        session['times_visited'] += 1
    else:
        session['times_visited'] = 1
    
    if 'times_actually_visited' in session:
        session['times_actually_visited'] += 1
    else:
        session['times_actually_visited'] = 1
    return render_template("index.html")

@app.route('/plus_two', methods=['POST'])
def plus_two():
    session['times_visited'] += 1
    return redirect('/')

@app.route('/plus_increment', methods=['POST'])
def plus_increment():
    session['times_visited'] += int(request.form['num_times']) - 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.pop('times_visited')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)