
from flask import Flask, render_template, url_for, request, session, redirect

app = Flask(__name__)    
app.secret_key = 'rabotaetspecnaz'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username

        if username == 'dima' and password == 'pass':
            return redirect(url_for('secpage'), code=301)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('index.html', error=error)

@app.route('/secpage', methods=['GET', 'POST'])
def secpage():
    username = session['username']
    return render_template('secpage.html', username = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
