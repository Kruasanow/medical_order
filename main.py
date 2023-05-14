
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
        from get_from_db import get_data_from_db
        from hash import hashed_data
        passw = str(get_data_from_db('clients','pass','name',username)).replace('[','').replace(']','').replace(')','').replace('(','').replace("'",'').replace(",",'')
        password = hashed_data(password)
        if passw == password:
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
