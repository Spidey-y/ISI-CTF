# check for database else create it
import sqlite3


def init_db():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(
            'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        conn.commit()
        conn.close()
    except Exception as e:
        return False
    return True

# insert user into database


def insert_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES ("' +
                  username+'", "'+password+'")')
        conn.commit()
        conn.close()
    except Exception as e:
        return False
    return True


def check_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT username FROM users WHERE username = "' +
                  username+'" AND password = "'+password+'"')
        result = c.fetchone()
        conn.commit()
        conn.close()
        if result:
            return result
    except Exception as e:
        return False
    return False
