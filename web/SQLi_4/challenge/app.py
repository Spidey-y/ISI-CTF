import hashlib
import re
from util import check_db, check_user, insert_user
from flask import Flask, render_template, request
import os

app = Flask(__name__)
flag = os.environ.get('FLAG', 'flag{fake_flag}')


def validate_input(s):
    blacklist = ['" ', ' "', "'", '`', ' `', '` ', '>', '<']
    if '"' in s:
        if not re.search(r'[0-9a-zA-Z]"[0-9a-zA-Z]', s):
            return True
    for token in blacklist:
        if token in s:
            return True
    return False


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_input(username):
            return render_template('login.html', message="Hacking attempt detected!")
        result = check_user(username, password)
        if result:
            pwd_hash, salt = result[1].split('$')
            if pwd_hash == hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest():
                return "Welcome! here's your flag: <h3>"+flag+"</h3>"
        return render_template('login.html', message="Invalid username or password")
    return render_template('login.html')


check_db()
