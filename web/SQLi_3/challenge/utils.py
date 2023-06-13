# create products db
import sqlite3
import string
import random
import os

flag = os.environ.get('FLAG', 'flag{test_flag}')


def create_db():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS products')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, price INTEGER)''')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    tmp1 = ''.join(random.choice(string.ascii_lowercase) for i in range(30))
    tmp2 = ''.join(random.choice(string.ascii_lowercase) for i in range(30))
    c.execute('''CREATE TABLE IF NOT EXISTS '''+tmp1 +
              '''(id INTEGER PRIMARY KEY, '''+tmp2+''' TEXT)''')
    conn.commit()
    conn.close()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''INSERT INTO '''+tmp1+''' ('''+tmp2 +
              ''') VALUES ("'''+flag+'''")''')
    conn.commit()
    conn.close()


def search_for_product(search):
    try:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products WHERE name LIKE '%"+search+"%'")
        result = c.fetchall()
        conn.commit()
        conn.close()
        if result:
            return result
    except Exception as e:
        print(e)
        return False
    return False

# add product


def add_product(name, price):
    try:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute("INSERT INTO products (name, price) VALUES (?, ?)",
                  (name, price))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        return False
    return True

# insert items


def fill():
    add_product('apple', 10)
    add_product('banana', 20)
    add_product('orange', 30)
    add_product('pineapple', 40)
    add_product('grape', 50)
    add_product('watermelon', 60)
    add_product('melon', 70)
    add_product('strawberry', 80)
