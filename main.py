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
        print(passw)
        print(password)
        # if passw == '1':
        if passw == password:
            return redirect(url_for('secpage'), code=301)
        else:
            error = 'Неверный пароль.'
    return render_template('index.html', error=error)


def sett(www):
    key='11100100'*len(www)
    deca=list(www)
    deca=[bin(ord(i))[-8::] for i in www]
    for i in range(len(deca)):
        if 'b' in deca[i]:
            deca[i]=deca[i].replace('b', '0')
    q=''    
    xorres=''
    dec=''
    qqq=''
    for i in deca:
        q=q+i
    for i in range(len(key)):
        xorres=int(key[i])^int(q[i])
        qqq+=str(xorres)
    decc=[qqq[i:i+8] for i in range(0, len(qqq), 8)]
    for i in range(len(decc)):
        decc[i]=int(decc[i],2)
        decc[i]=chr(int(decc[i]))
        dec+=decc[i]
    return dec

@app.route('/secpage', methods=['GET', 'POST'])
def secpage():
    username = session['username']
    from get_from_db import insert_data_by_name, insert_code
    if request.method == 'POST':
        client_code = request.form['client_code']
        fio = request.form['fio']
        address = request.form['address'] 
        phone = request.form['phone']
        email = request.form['email']
        other_data = request.form['other_data']
        animal_code = request.form['animal_code']
        kind = request.form['kind']
        poroda = request.form['poroda']
        klichka = request.form['klichka']
        sex = request.form['sex']
        bday = request.form['bday']
        color = request.form['color']
        info = request.form['info']
        print('encrypt: ',client_code,fio,address,phone,email,other_data,animal_code,kind,poroda,klichka,sex,bday,color,info)
        


        c_client_code = sett(client_code)
        c_fio = sett(fio)
        c_address = sett(address)
        c_phone = sett(phone)
        c_email = sett(email)
        c_other_data = sett(other_data)
        insert_data_by_name('clients','client_code',c_client_code,session['username'],'name')
        insert_data_by_name('clients','address',c_address,session['username'],'name')
        insert_data_by_name('clients','phone',c_phone,session['username'],'name')
        insert_data_by_name('clients','email',c_email,session['username'],'name')
        insert_data_by_name('clients','other_data',c_other_data,session['username'],'name')
        insert_code('animals','client_code',c_client_code)

        a_animal_code = sett(animal_code)
        a_kind = sett(kind)
        a_poroda = sett(poroda)
        a_klichka = sett(klichka)
        a_client_code = sett(client_code)
        a_sex = sett(sex)
        a_bday = sett(bday)
        a_color = sett(color)
        a_info = sett(info)

        insert_data_by_name('animals','animal_code',a_animal_code,a_client_code,'client_code')
        insert_data_by_name('animals','kind',a_kind,a_client_code,'client_code')
        insert_data_by_name('animals','poroda',a_poroda,a_client_code,'client_code')
        insert_data_by_name('animals','klichka',a_klichka,a_client_code,'client_code')
        # insert_data_by_name('animals','client_code',a_client_code,session['username'],'name')
        insert_data_by_name('animals','sex',a_sex,a_client_code,'client_code')
        insert_data_by_name('animals','bday',a_bday,a_client_code,'client_code')
        insert_data_by_name('animals','color',a_color,a_client_code,'client_code')
        insert_data_by_name('animals','info',a_info,a_client_code,'client_code')

        print('decrypt: ',c_client_code, c_fio, c_address, c_phone, c_email, c_other_data, a_animal_code, a_kind, a_poroda, a_klichka, a_client_code, a_sex, a_bday, a_color, a_info)
        print(a_animal_code, a_kind, a_poroda, a_klichka, a_client_code, a_sex, a_bday, a_color, a_info)
        
        return render_template('secpage.html', username = username) 

    return render_template('secpage.html', username = username)

@app.route('/threepage', methods=['GET', 'POST'])
def threepage():
    username = session['username']
    from get_from_db import insert_data_by_name, insert_code
    from db_do import get_db_connection
    if request.method == 'POST':
        if 'animal_kind_code' in request.form:
            animal_kind_code = request.form['animal_kind_code']
            kind_animal_name = request.form['kind_animal_name']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO animal_type ('
                            'animal_kind_code, kind_animal_name)'
                    'VALUES ('
                            '%s, %s)',
                            (
                str(animal_kind_code),
                str(kind_animal_name),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'num_in_journal' in request.form:
            num_in_journal = request.form['num_in_journal']
            worker = request.form['worker']
            usluga_code = request.form['usluga_code']
            quantity = request.form['quantity']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO current_uslugi ('
                            'num_in_journal, worker, usluga_code, quantity)'
                    'VALUES ('
                            '%s, %s, %s, %s)',
                            (
                str(num_in_journal),
                str(worker),
                str(usluga_code),
                str(quantity),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'journal_number' in request.form:
            journal_number = request.form['journal_number']
            date = request.form['date']
            client = request.form['client']
            animal_code = request.form['animal_code']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO journal ('
                            'journal_number, date, client, animal_code)'
                    'VALUES ('
                            '%s, %s, %s, %s)',
                            (
                str(journal_number),
                str(date),
                str(client),
                str(animal_code),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'medicament_code' in request.form:
            medicament_code = request.form['medicament_code']
            medicament_name = request.form['medicament_name']
            description = request.form['description']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO medicaments ('
                            'medicament_code, medicament_name, description)'
                    'VALUES ('
                            '%s, %s, %s)',
                            (
                str(medicament_code),
                str(medicament_name),
                str(description),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'poroda_code' in request.form:
            poroda_code = request.form['poroda_code']
            kind_of_animal = request.form['kind_of_animal']
            porodas_name = request.form['porodas_name']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO poroda ('
                            'poroda_code, kind_of_animal, porodas_name)'
                    'VALUES ('
                            '%s, %s, %s)',
                            (
                str(poroda_code),
                str(kind_of_animal),
                str(porodas_name),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'rank_code' in request.form:
            rank_code = request.form['rank_code']
            name = request.form['name']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO rank ('
                            'rank_code, name)'
                    'VALUES ('
                            '%s, %s)',
                            (
                str(rank_code),
                str(name),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'jnumber' in request.form:
            jnumber = request.form['jnumber']
            njournal = request.form['njournal']
            medical_code = request.form['medical_code']
            aem = request.form['aem']
            price = request.form['price']
            quantity = request.form['quantity']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO used_medical ('
                            'journal_number, num_in_journal, medical_code, aem, price, quantity)'
                    'VALUES ('
                            '%s, %s, %s, %s, %s, %s)',
                            (
                str(jnumber),
                str(njournal),
                str(medical_code),
                str(aem),
                str(price),
                str(quantity),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 
        
        if 'usluga_code' in request.form:
            usluga_code = request.form['usluga_code']
            usluga_name = request.form['usluga_name']
            price = request.form['price']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO uslugi ('
                            'usluga_code, usluga_name, price)'
                    'VALUES ('
                            '%s, %s, %s)',
                            (
                str(usluga_code),
                str(usluga_name),
                str(price),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 

        if 'worker_code' in request.form:
            worker_code = request.form['worker_code']
            name = request.form['name']
            address = request.form['address']
            phone = request.form['phone']
            email = request.form['email']
            description = request.form['description']
            rank = request.form['rank']
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO workers ('
                            'worker_code, name, address, phone, email, description, rank)'
                    'VALUES ('
                            '%s, %s, %s, %s, %s, %s, %s)',
                            (
                str(worker_code),
                str(name),
                str(address),
                str(phone),
                str(email),
                str(description),
                str(rank),
                )
                )
            conn.commit()
            cur.close()
            conn.close()
            return render_template('threepage.html') 
            
        return render_template('threepage.html', username = username) 

    return render_template('threepage.html', username = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
