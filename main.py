
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
    from get_from_db import insert_data_by_name, insert_code
    if request.method == 'POST':

        c_client_code = request.form['client_code']
        c_fio = request.form['fio']
        c_address = request.form['address'] 
        c_phone = request.form['phone']
        c_email = request.form['email']
        c_other_data = request.form['other_data']
        insert_data_by_name('clients','client_code',c_client_code,session['username'],'name')
        insert_data_by_name('clients','address',c_address,session['username'],'name')
        insert_data_by_name('clients','phone',c_phone,session['username'],'name')
        insert_data_by_name('clients','email',c_email,session['username'],'name')
        insert_data_by_name('clients','other_data',c_other_data,session['username'],'name')
        insert_code('animals','client_code',c_client_code)

        a_animal_code = request.form['animal_code']
        a_kind = request.form['kind']
        a_poroda = request.form['poroda']
        a_klichka = request.form['klichka']
        a_client_code = request.form['client_code']
        a_sex = request.form['sex']
        a_bday = request.form['bday']
        a_color = request.form['color']
        a_info = request.form['info']
        insert_data_by_name('animals','animal_code',a_animal_code,a_client_code,'client_code')
        insert_data_by_name('animals','kind',a_kind,a_client_code,'client_code')
        insert_data_by_name('animals','poroda',a_poroda,a_client_code,'client_code')
        insert_data_by_name('animals','klichka',a_klichka,a_client_code,'client_code')
        # insert_data_by_name('animals','client_code',a_client_code,session['username'],'name')
        insert_data_by_name('animals','sex',a_sex,a_client_code,'client_code')
        insert_data_by_name('animals','bday',a_bday,a_client_code,'client_code')
        insert_data_by_name('animals','color',a_color,a_client_code,'client_code')
        insert_data_by_name('animals','info',a_info,a_client_code,'client_code')

        print(c_client_code, c_fio, c_address, c_phone, c_email, c_other_data)
        print(a_animal_code, a_kind, a_poroda, a_klichka, a_client_code, a_sex, a_bday, a_color, a_info)
        
        return render_template('secpage.html', username = username) 

    return render_template('secpage.html', username = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
