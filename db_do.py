import os
import psycopg2 as ps

def get_db_connection():
    conn = ps.connect(host='localhost',
                      database='medical_db', #postgres
                      user='anna',           #postgres
                      password='anna'
                    )
    return conn

conn = get_db_connection()

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS clients;')
#Клиенты - clients
try:
    cur.execute('CREATE TABLE clients (id serial PRIMARY KEY,' 
                                 'client_code varchar (200),'
                                 'name varchar (200),'
                                 'pass varchar (200),'
                                 'address varchar (200),'
                                 'phone varchar (200),'
                                 'email varchar (200),'
                                 'other_data varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base clients already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS animal_type;')
#Вид животного - animal_type
try:
    cur.execute('CREATE TABLE animal_type (id serial PRIMARY KEY,' 
                                 'animal_kind_code varchar (200),'
                                 'kind_animal_name varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base animal_type already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS animals;')
#Животные - animals
try:
    cur.execute('CREATE TABLE animals (id serial PRIMARY KEY,' 
                                 'animal_code varchar (200),'
                                 'kind varchar (200),'
                                 'poroda varchar (200),'
                                 'klichka varchar (200),'
                                 'client_code varchar (200),'
                                 'sex varchar (200),'
                                 'bday varchar (200),'
                                 'color varchar (200),'
                                 'info varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base animals already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS poroda;')
#Порода - poroda
try:
    cur.execute('CREATE TABLE poroda (id serial PRIMARY KEY,' 
                                 'poroda_code varchar (200),'
                                 'kind_of_animal varchar (200),'
                                 'porodas_name varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base poroda already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS journal;')
#Жунрал - journal
try:
    cur.execute('CREATE TABLE journal (id serial PRIMARY KEY,' 
                                 'journal_number varchar (200),'
                                 'date varchar (200),'
                                 'client varchar (200),'
                                 'animal_code varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base journal already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS used_medical;')
#Использованные медикаменты - used_medical
try:
    cur.execute('CREATE TABLE used_medical (id serial PRIMARY KEY,' 
                                 'journal_number varchar (200),'
                                 'num_in_journal varchar (200),'
                                 'medical_code varchar (200),'
                                 'aem varchar (200),'
                                 'price varchar (200),'
                                 'quantity varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base used_medical already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS current_uslugi;')
#Оказанные услуги - current_uslugi
try:
    cur.execute('CREATE TABLE current_uslugi (id serial PRIMARY KEY,' 
                                 'num_in_journal varchar (200),'
                                 'worker varchar (200),'
                                 'usluga_code varchar (200),'
                                 'quantity varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base current_uslugi already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS uslugi;')
#Услуги - uslugi
try:
    cur.execute('CREATE TABLE uslugi (id serial PRIMARY KEY,' 
                                 'usluga_code varchar (200),'
                                 'usluga_name varchar (200),'
                                 'price varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base uslugi already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS medicaments;')
#Услуги - medicaments
try:
    cur.execute('CREATE TABLE medicaments (id serial PRIMARY KEY,' 
                                 'medicament_code varchar (200),'
                                 'medicament_name varchar (200),'
                                 'description varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base medicaments already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS workers;')
#Услуги - workers
try:
    cur.execute('CREATE TABLE workers (id serial PRIMARY KEY,' 
                                 'worker_code varchar (200),'
                                 'name varchar (200),'
                                 'address varchar (200),'
                                 'phone varchar (200),'
                                 'email varchar (200),'
                                 'description varchar (200),'
                                 'rank varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base workers already exist!')
    conn.rollback()

# cur.execute('DROP TABLE IF EXISTS rank;')
#Услуги - rank
try:
    cur.execute('CREATE TABLE rank (id serial PRIMARY KEY,' 
                                 'rank_code varchar (200),'
                                 'name varchar (200),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
except Exception:
    print('base rank already exist!')
    conn.rollback()

conn.commit()
cur.close()
conn.close()

