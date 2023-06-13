#check for database else create it
import sqlite3
import uuid


def check_db():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS users')
        conn.commit()
        conn.close()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        conn.commit()
        conn.close()
        salt = str(uuid.uuid4()).replace("-","")
        password = str(uuid.uuid4()).replace("-","")+"$"+salt
        insert_user("admin", password=password)
    except Exception as e:
        print(e)
        return False
    return True

#insert user into database
def insert_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES ("'+username+'", "'+password+'")')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        return False
    return True


def check_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT username, password FROM users WHERE username = "'+username+'"')
        result = c.fetchone()
        conn.commit()
        conn.close()
        if result:
            return result
    except Exception as e:
        print(e)
        return False
    return False

 