from util import init_db, check_user, insert_user
from flask import Flask, render_template, request
import os

app = Flask(__name__)
flag = os.environ.get('FLAG', 'flag{test_flag}')


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = check_user(username, password)
        if result:
            return "Welcome! here's your flag: "+result[0]
        else:
            return render_template('login.html', message="Invalid username or password")
    return render_template('login.html')


init_db()
insert_user("admin", flag)
