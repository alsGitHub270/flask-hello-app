import os
import logging

from flask import Flask, request, render_template, redirect, url_for, flash, session
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password for user (%s)",
                                request.form.get('username'))
                                
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))
    

def valid_login(username, password):
    if username == password:
        return True
    return False
    

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')   # for cloud 9
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.secret_key = '\x96\xfd\xc9@b\xd5\xec\xe8}H\xbb\xa0\x83\xf1l\xaa\xa3\x88\x00z\xcf\xe8\xb8\t'
    
    #logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    
    app.run(host=host, port=port)