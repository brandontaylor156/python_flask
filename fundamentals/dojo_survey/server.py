from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'brando'

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/submit_form', methods=['POST'])
def submit_form():
    session['name'] = request.form['your_name']
    session['location'] = request.form['your_location']
    session['language'] = request.form['your_language']
    session['comment'] = request.form['comment']
    session['level'] = request.form['fun_level']
    if 'spirit_animal[]' in request.form:
            session['spirit_animal'] = request.form['spirit_animal[]']
    return redirect('/result')

@app.route('/result')
def result():
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    level = session['level']
    if 'spirit_animal' in session:
        spirit_animal = session['spirit_animal']
    session.clear()
    return render_template("result.html", name=name, location=location, language=language, comment=comment, level=level, animal=spirit_animal)


if __name__=="__main__":
    app.run(debug=True)