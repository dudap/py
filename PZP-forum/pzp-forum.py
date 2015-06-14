#-*- coding: utf-8 -*-
# all the imports
#!/usr/bin/env python
from funktion import hasloo, delay, Entropy
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, make_response
from contextlib import closing
from timer import czas
from OpenSSL import SSL
import smtplib
from send_mail import maillll 
# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'

PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)

app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
	with app.open_resource('schema.sql', mode='r') as f:
	    db.cursor().executescript(f.read())
	db.commit()


@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
#-------------------------------------------------------------------------
@app.route('/')
def show_entries():
    cur = g.db.execute('select autor, text,time from entries order by id desc')
    entries = [dict(autor=row[0], text=row[1],time=row[2]) for row in cur.fetchall()]

    return render_template('show_entries.html', entries=entries)
#-------------------------------------------------------------------------
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('username'):
        abort(401)
    h=request.form['text']
    a=(str((str(request.form['text']))))
    
    g.db.execute('insert into entries (autor, text,time) values (?, ?,?)',
                 [session['username'], qwerty(h),czas()])
    g.db.commit()
    flash('Dodano post')
    return redirect(url_for('show_entries'))
#-------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	cur = g.db.execute('select autor, password from users order by id desc')
    entries = [dict(autor=row[0], password=row[1]) for row in cur.fetchall()]
	a=0
	for entry in entries:
		if entry['autor']==qwerty(hasloo(request.form['username'])) and qwerty(hasloo(request.form['password']))==entry['password']:
			session['username'] = qwerty(request.form['username'])
			delay()
           		flash('Zalogowany')
			delay()
			a=1
            		return redirect(url_for('show_entries'))
	if a==0:
		error=u'Błędne dane'
    return render_template('login.html', error=error)
#-------------------------------------------------------------------------
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Wylogowano')
    return redirect(url_for('show_entries'))
#-------------------------------------------------------------------------
@app.route('/check_password', methods=['GET', 'POST'])
def check_password():
    error = None
    if request.method == 'POST':
	cur = g.db.execute('select autor, password from users order by id desc')
        entries = [dict(autor=row[0], password=row[1]) for row in cur.fetchall()]
	a=0
	for entry in entries:
		if entry['autor']==hasloo(session['username']) and qwerty(hasloo(request.form['password']))==entry['password']:
			
			g.db.execute ("UPDATE users SET password=? WHERE autor=?", (qwerty(hasloo(request.form['password1'])),hasloo(session['username'])) )
			g.db.commit()
			flash(u'Hasło zostało zmienione')
			a=1
			return redirect(url_for('check_password'))
      	if a==0:
		error=u'Błędne dane'
	
    return render_template('check_password.html', error=error)
#-------------------------------------------------------------------
@app.route('/check_mail', methods=['GET', 'POST'])
def check_mail():
    error = None
    if request.method == 'POST':
	cur = g.db.execute('select autor, password,mail from users order by id desc')
        entries = [dict(autor=row[0], password=row[1],mail=row[2]) for row in cur.fetchall()]
	a=0
	for entry in entries:
		if entry['mail']==qwerty(hasloo(request.form['mail'])):
			flash(u'Adres E-mail znajduje się już w bazie')			
			return redirect(url_for('check_mail'))
		if entry['autor']==hasloo(session['username']) and qwerty(hasloo(request.form['password']))==entry['password']:
			
			g.db.execute ("UPDATE users SET mail=? WHERE autor=?", (hasloo(qwerty(request.form['mail'])),hasloo(session['username'])) )
			g.db.commit()
			flash(u'Email został zmieniony.')
					
			a=1
			return redirect(url_for('check_mail'))
      	if a==0:
		error=u'Błędne dane'
	
    return render_template('check_mail.html', error=error)
#-------------------------------------------------------------------

@app.route('/profile')
def profile():
    i=0
    q=[]
    
    #del session['admin']
    print session
    cur = g.db.execute('select autor, text , time from entries order by id desc')
    entries = [dict(autor=row[0], text=row[1], time=row[2]) for row in cur.fetchall()]
    for entry in entries:
	if entry['autor']==session['username']:
		q.append(entry)
		
    #entries=entry
    return render_template('profile.html', entries=q)

#-------------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
	if request.form['password']!=request.form['password2']:
		flash(u'Hasła nie są takie same')
		return redirect(url_for('register'))
	elif len(request.form['password'])<8 :
		flash(u'Zbyt mala liczba znaków')
		return redirect(url_for('register'))
	elif Entropy(request.form['password'])<2:
		flash(u'Hasło jest zbyt słabe')
		return redirect(url_for('register'))
	cur = g.db.execute('select autor, mail from users order by id desc')
        entries = [dict(autor=row[0], mail=row[1]) for row in cur.fetchall()]
	for entry in entries:
		if entry['autor']==qwerty(hasloo(request.form['username'])):
			flash(u'Użytkownik już istnieje')
			return redirect(url_for('register'))
	for entry in entries:
		if entry['mail']==qwerty(hasloo(request.form['mail'])):
			flash(u'Mail już znajduje się w bazie')
			return redirect(url_for('register'))
	else:
		g.db.execute('insert into users (autor, password, mail,token,change) values (?, ?,?,?,?)',[ qwerty(hasloo(request.form['username'])), qwerty(hasloo(request.form['password'])),qwerty(hasloo(request.form['mail'])),'','no'])
 	        g.db.commit()
		delay()
		session['username'] = qwerty(request.form['username'])
        	flash('Zarejestrowany')
        	return redirect(url_for('show_entries'))
    return render_template('register.html', error=error)

#-------------------------------------------------------------------------
@app.route('/miss', methods=['GET', 'POST'])
def miss():
    error = None
    if request.method == 'POST':
       cur = g.db.execute('select autor, mail from users order by id desc')
       entries = [dict(autor=row[0], mail=row[1]) for row in cur.fetchall()]
       for entry in entries:
		if entry['autor']==qwerty(hasloo(request.form['username'])) and qwerty(hasloo(request.form['mail']))==entry['mail']:
          		d=maillll(request.form['mail'])
			flash(u'Wysłano')			
			g.db.execute ("UPDATE users SET change=? ,token=? WHERE autor=?", ('yes',d,qwerty(hasloo(request.form['username']))) )
			print d
			g.db.commit()
			return redirect(url_for('check_password2'))
	  		
		
        	else:
            		error=u'Błędne dane'
    return render_template('miss.html', error=error)
#-----------------------------------------------------------------------
@app.route('/check_password2', methods=['GET', 'POST'])
def check_password2():
    error = None
    if request.method == 'POST':
	cur = g.db.execute('select token, change from users order by id desc')
        entries = [dict(token=row[0], change=row[1]) for row in cur.fetchall()]
	a=0
	for entry in entries:
		if qwerty(entry['token'])==qwerty(request.form['token']) and entry['change']=='yes':
			g.db.execute ("UPDATE users SET password=? ,change=? WHERE token=?", (qwerty(hasloo(request.form['password2'])),'no',qwerty(request.form['token'])) )
			g.db.commit()
			flash(u'Zmieniono hasło')
			a=1
			return redirect(url_for('login'))
      	if a==0:
		error=u'błędne dane'
		return render_template('check_password2.html', error=error)
    return render_template('check_password2.html', error=error)
#-------------------------------------------------------------------------
def qwerty(tekst):
	napis_zrodlowy = str(tekst)
	text = ''
	for c in napis_zrodlowy: 
	  if(c=='<'):
	    c='&lt;'
	  if c=='>':
            c='&gt;'
	  if c=='&':
	    c='&amp;'
	  if c=='\'':
	    c='&acute;'
	  text+=c
	
	return text
	

#----------------------------------------------------------------------------
if __name__ == '__main__':
	
	context = ('apache.crt', 'apache.key')
	app.run(host='10.0.2.15', port=8110, ssl_context=context)
	
