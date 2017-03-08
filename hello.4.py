import os

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        return "User %s logged in" %request.form['username']
    return render_template('login.html')


def valid_login(username, password):
    if username == password:
        return True
    return False

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')   # for cloud 9
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.run(host=host, port=port)